# lmdb 非法地址写

## Description

```
An issue was discovered in py-lmdb 0.97.With a wrong value of mp_flags,mdb node add function in lib/mdb.c will write data to an illegal address.
```

## Version

version <=0.97

https://github.com/jnwatson/py-lmdb

## Vuln Detail

In function `mdb_page_touch`，`mp_flags` determines the value of `mc->mc_pg[mc->mc_top]`.

```c
#define	P_DIRTY		 0x10
#define F_ISSET(w, f)	 (((w) & (f)) == (f))
static int
mdb_page_touch(MDB_cursor *mc)
{
	MDB_page *mp = mc->mc_pg[mc->mc_top], *np;
	MDB_txn *txn = mc->mc_txn;
	MDB_cursor *m2, *m3;
	pgno_t	pgno;
	int rc;

	if (!F_ISSET(mp->mp_flags, P_DIRTY)) {
		if (txn->mt_flags & MDB_TXN_SPILLS) {
			np = NULL;
            //np is first assigned mp
			rc = mdb_page_unspill(txn, mp, &np);
			……
		}
        //In normal mdb file,mp_flags=0x2,np returns to a heap address alloc by mdb_page_alloc
		if ((rc = mdb_midl_need(&txn->mt_free_pgs, 1)) ||
			(rc = mdb_page_alloc(mc, 1, &np)))
			goto fail;
		……
	} else if (txn->mt_parent && !IS_SUBP(mp)) {
		……
	} else {
        //With a wrong mp_flags(e.g. mp_flags=0x12),np returns with the value of mp
		return 0;
	}
	……

done:
  	//In the right procedure,mc_pg[mc->mc_top] is assigned np,which is a heap address
    //But with the wrong mp_flags,np point to mp,which is a address of data.mdb,without write permission
	mc->mc_pg[mc->mc_top] = np;
	……
	return 0;

fail:
	txn->mt_flags |= MDB_TXN_ERROR;
	return rc;
}
```

If there is a `put` action,`mdb_node_add` function will write data to `mc->mc_pg[mc->top]`.

```c
static int
mdb_node_add(MDB_cursor *mc, indx_t indx,
    MDB_val *key, MDB_val *data, pgno_t pgno, unsigned int flags)
{
	unsigned int	 i;
	size_t		 node_size = NODESIZE;
	ssize_t		 room;
	indx_t		 ofs;
	MDB_node	*node;
    //assignment
	MDB_page	*mp = mc->mc_pg[mc->mc_top];
	……
	update:
	/* Move higher pointers up one slot. */
  
	for (i = NUMKEYS(mp); i > indx; i--)
		mp->mp_ptrs[i] = mp->mp_ptrs[i - 1];//mp point to mc->mc_pg[mc->top]
	……
}
```

## Debug

```c
RAX  0x7efff5997002 ◂— 0x0
 RBX  0x7efff5997000 ◂— 0x2
 RCX  0xfe8
 RDX  0x14
 RDI  0x7efff5997000 ◂— 0x2
 RSI  0xfe8
 R8   0x0
 R9   0x0
 R10  0x0
 R11  0xffffffffffffffff
 R12  0x7fffffff9900 ◂— 0x1
 R13  0x7fffffff9540 ◂— 0x0
 R14  0xc
 R15  0x7fffffff9910 ◂— 0x3
 RBP  0x0
 RSP  0x7fffffff93a0 —▸ 0x7efff5997004 ◂— 0x12000000000000
 RIP  0x7ffff5ca5fca (mdb_node_add+442) ◂— mov    word ptr [rax + 0x12], si
──────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────
 ► 0x7ffff5ca5fca <mdb_node_add+442>    mov    word ptr [rax + 0x12], si
   0x7ffff5ca5fce <mdb_node_add+446>    cmp    rdi, rax
   0x7ffff5ca5fd1 <mdb_node_add+449>    jne    mdb_node_add+432 <0x7ffff5ca5fc0>
    ↓
   0x7ffff5ca5fc0 <mdb_node_add+432>    movzx  esi, word ptr [rax + r11*2 + 0x10]
   0x7ffff5ca5fc6 <mdb_node_add+438>    sub    rax, 2
 ► 0x7ffff5ca5fca <mdb_node_add+442>    mov    word ptr [rax + 0x12], si
   0x7ffff5ca5fce <mdb_node_add+446>    cmp    rdi, rax
   0x7ffff5ca5fd1 <mdb_node_add+449>    jne    mdb_node_add+432 <0x7ffff5ca5fc0>
 
   0x7ffff5ca5fd3 <mdb_node_add+451>    sub    ecx, r14d
   0x7ffff5ca5fd6 <mdb_node_add+454>    movzx  eax, dx
   0x7ffff5ca5fd9 <mdb_node_add+457>    movzx  esi, cx
───────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────
In file: /home/yt360/yt/crashes/py-lmdb/lib/mdb.c
   7300 		goto full;
   7301 
   7302 update:
   7303 	/* Move higher pointers up one slot. */
   7304 	for (i = NUMKEYS(mp); i > indx; i--)
 ► 7305 		mp->mp_ptrs[i] = mp->mp_ptrs[i - 1];
   7306 
   7307 	/* Adjust free space offsets. */
   7308 	ofs = mp->mp_upper - node_size;
   7309 	mdb_cassert(mc, ofs >= mp->mp_lower + sizeof(indx_t));
   7310 	mp->mp_ptrs[indx] = ofs;
───────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffff93a0 —▸ 0x7efff5997004 ◂— 0x12000000000000
01:0008│      0x7fffffff93a8 —▸ 0x694580 ◂— 0x0
02:0010│      0x7fffffff93b0 —▸ 0x7ffff7f192e8 —▸ 0x7ffff7580b00 (_Py_NoneStruct) ◂— 0x64e
03:0018│      0x7fffffff93b8 ◂— 0x1
04:0020│      0x7fffffff93c0 ◂— 0x0
05:0028│      0x7fffffff93c8 ◂— 0xe4e474bd3c9cae00
06:0030│      0x7fffffff93d0 —▸ 0x7ffff7f199d4 ◂— '/tmp/_MEIiDWmyn/eggs'
07:0038│      0x7fffffff93d8 —▸ 0x7fffffff9540 ◂— 0x0
─────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────
 ► f 0     7ffff5ca5fca mdb_node_add+442
   f 1     7ffff5ca9649 mdb_cursor_put+2521
   f 2     7ffff5caba2b mdb_put+251
   f 3     7ffff5c9f300 trans_put+256
   f 4     7ffff70f41b3 PyEval_EvalFrameEx+28659
   f 5     7ffff7225278 PyEval_EvalCodeEx+2008
   f 6     7ffff70ed029 PyEval_EvalCode+25
   f 7           402ca1
   f 8           403087
   f 9     7ffff75e4b97 __libc_start_main+231
Program received signal SIGSEGV (fault address 0x7efff5997014)
```
## others
```
please send email to teamseri0us360@gmail.com if you have any questions.
```
