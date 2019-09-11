# lmdb 地址未初始化漏洞

## Description

```
 An issue was dicovered in py-lmdb 0.97.With a wrong value of field md_flag,it can bypass the initialization of mv_data,writing to an illegal address.
```

## Version

version <=0.97

https://github.com/jnwatson/py-lmdb

## Vuln Detail

In function `mdb_cursor_put`,the value of `md_flags` determines the value of `mp_flags`.

```c
if ((mc->mc_db->md_flags & (MDB_DUPSORT|MDB_DUPFIXED))
			== MDB_DUPFIXED)
  //MDB_DUPSORT 0x4;MDB_DUPFIXED 0x10
			np->mp_flags |= P_LEAF2;
```

In normal `data.mdb`,`md_flags=0x8`,so the value of `mp_flags` won't change.With a wrong value of `md_flags` such as `0x18`,`mp_flags` adds the `P_LEAF2`.

At last,when commiting the transaction,function `mdb_node_add` will execute.

```c
#define IS_LEAF2(p)	 F_ISSET((p)->mp_flags, P_LEAF2) #P_LEAF2 0x20
#define F_ISSET(w, f)	 (((w) & (f)) == (f))
#define LEAF2KEY(p, i, ks)	((char *)(p) + PAGEHDRSZ + ((i)*(ks)))
static int
mdb_node_add(MDB_cursor *mc, indx_t indx,
    MDB_val *key, MDB_val *data, pgno_t pgno, unsigned int flags)
{
	unsigned int	 i;
	size_t		 node_size = NODESIZE;
	ssize_t		 room;
	indx_t		 ofs;
	MDB_node	*node;
	MDB_page	*mp = mc->mc_pg[mc->mc_top];
	……
    //With wrong md_flags,mp_flags added P_LEAF2 in last step,this part will execute
    //In normal condition,this part won't execute
	if (IS_LEAF2(mp)) {
		……
      	mp->mp_lower += sizeof(indx_t);
		mp->mp_upper -= ksize - sizeof(indx_t);
		//return here,data->mv_data is not assigned
        return MDB_SUCCESS;
	}
    ……
    //In normal condition,mv_data is assigned here
    data->mv_data = ndata;
  	……
}
```

After `mdb_cursor_put` is called by `mdb_freelist_save`, data.mv_data is used as the destination address of `memcpy`.

```c
static int
mdb_freelist_save(MDB_txn *txn)
{
	……

	for (;;) {
		MDB_val key, data;
		pgno_t *pgs;
		ssize_t j;

		……
		if (freecnt < txn->mt_free_pgs[0]) {
			……
			do {
				freecnt = free_pgs[0];
				data.mv_size = MDB_IDL_SIZEOF(free_pgs);
				rc = mdb_cursor_put(&mc, &key, &data, MDB_RESERVE);
				……
			} while (freecnt < free_pgs[0]);
			mdb_midl_sort(free_pgs);
            //The destination address of memcpy is not initialized and is a non-writable address.
			memcpy(data.mv_data, free_pgs, data.mv_size);
		 ……
        }
      ……
    }
  ……
}
```

## Debug

```c
 RAX  0x5555556267f7 ◂— mov    rcx, qword ptr [rbp + 0x10]
 RBX  0x555555bb9340 ◂— 0x0
 RCX  0x0
 RDX  0x10
 RDI  0x5555556267f7 ◂— mov    rcx, qword ptr [rbp + 0x10]
 RSI  0x7ffff6113018 ◂— 0x1
 R8   0x2
 R9   0x10000
 R10  0x555555bad310 —▸ 0x7ffff7dcfca0 (main_arena+96) —▸ 0x555555bc4d80 ◂— 0x0
 R11  0x1
 R12  0x0
 R13  0x7fffffffd660 ◂— 0x0
 R14  0x0
 R15  0x555555b89d70 ◂— 0x300000004
 RBP  0x1
 RSP  0x7fffffffd548 —▸ 0x7ffff6227e89 (mdb_txn_commit+2345) ◂— jmp    0x7ffff6227950
 RIP  0x7ffff7b72b48 (__memmove_avx_unaligned_erms+120) ◂— vmovdqu xmmword ptr [rdi], xmm0
──────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────
 ► 0x7ffff7b72b48 <__memmove_avx_unaligned_erms+120>    vmovdqu xmmword ptr [rdi], xmm0
   0x7ffff7b72b4c <__memmove_avx_unaligned_erms+124>    vmovdqu xmmword ptr [rdi + rdx - 0x10], xmm1
   0x7ffff7b72b52 <__memmove_avx_unaligned_erms+130>    ret    
 
   0x7ffff7b72b53 <__memmove_avx_unaligned_erms+131>    mov    rcx, qword ptr [rsi + rdx - 8]
   0x7ffff7b72b58 <__memmove_avx_unaligned_erms+136>    mov    rsi, qword ptr [rsi]
   0x7ffff7b72b5b <__memmove_avx_unaligned_erms+139>    mov    qword ptr [rdi + rdx - 8], rcx
   0x7ffff7b72b60 <__memmove_avx_unaligned_erms+144>    mov    qword ptr [rdi], rsi
   0x7ffff7b72b63 <__memmove_avx_unaligned_erms+147>    ret    
 
   0x7ffff7b72b64 <__memmove_avx_unaligned_erms+148>    mov    ecx, dword ptr [rsi + rdx - 4]
   0x7ffff7b72b68 <__memmove_avx_unaligned_erms+152>    mov    esi, dword ptr [rsi]
   0x7ffff7b72b6a <__memmove_avx_unaligned_erms+154>    mov    dword ptr [rdi + rdx - 4], ecx
──────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd548 —▸ 0x7ffff6227e89 (mdb_txn_commit+2345) ◂— jmp    0x7ffff6227950
01:0008│      0x7fffffffd550 ◂— 0x5c0000006e /* 'n' */
02:0010│      0x7fffffffd558 —▸ 0x555555b89d70 ◂— 0x300000004
03:0018│      0x7fffffffd560 —▸ 0x7fffffffd5b0 ◂— 0x8
04:0020│      0x7fffffffd568 ◂— 0x0
05:0028│      0x7fffffffd570 —▸ 0x7fffffffd5c0 ◂— 0x10
06:0030│      0x7fffffffd578 ◂— 0x0
07:0038│      0x7fffffffd580 —▸ 0x7ffff6113018 ◂— 0x1
────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────
 ► f 0     7ffff7b72b48 __memmove_avx_unaligned_erms+120
   f 1     7ffff6227e89 mdb_txn_commit+2345
   f 2     7ffff6227e89 mdb_txn_commit+2345
   f 3     7ffff6227e89 mdb_txn_commit+2345
   f 4     7ffff6219e9d trans_commit+77
   f 5     55555564f8af PyEval_EvalFrameEx+22831
   f 6     555555647d0a PyEval_EvalCodeEx+1754
   f 7     555555647629 PyEval_EvalCode+25
   f 8     55555567861f
   f 9     555555673322 PyRun_FileExFlags+130
   f 10     55555567267d PyRun_SimpleFileExFlags+397
Program received signal SIGSEGV (fault address 0x5555556267f7)
pwndbg> bt
#0  __memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:293
#1  0x00007ffff6227e89 in memcpy (__len=<optimized out>, __src=0x7ffff6113018, __dest=<optimized out>) at /usr/include/x86_64-linux-gnu/bits/string_fortified.h:34
#2  mdb_freelist_save (txn=0x555555bb9340) at lib/mdb.c:3152
#3  mdb_txn_commit (txn=0x555555bb9340) at lib/mdb.c:3612
#4  0x00007ffff6219e9d in trans_commit (self=0x7ffff7fa3730) at lmdb/cpython.c:3087
#5  0x000055555564f8af in PyEval_EvalFrameEx ()
#6  0x0000555555647d0a in PyEval_EvalCodeEx ()
#7  0x0000555555647629 in PyEval_EvalCode ()
#8  0x000055555567861f in ?? ()
#9  0x0000555555673322 in PyRun_FileExFlags ()
#10 0x000055555567267d in PyRun_SimpleFileExFlags ()
#11 0x00005555556211ab in Py_Main ()
#12 0x00007ffff7a05b97 in __libc_start_main (main=0x555555620b10 <main>, argc=2, argv=0x7fffffffdd08, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdcf8) at ../csu/libc-start.c:310
#13 0x0000555555620a2a in _start () 
```

