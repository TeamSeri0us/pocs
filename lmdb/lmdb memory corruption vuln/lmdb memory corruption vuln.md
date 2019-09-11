# lmdb 内存损坏漏洞

## Description

```
An issue was discovered in py-lmdb 0.97.In mdb_node_del function in lib/mdb.c,there isn't any check on size before calling memmove,causing the dst parameter point to an illegal address or a heap address.
```

## Version

version <=0.97

https://github.com/jnwatson/py-lmdb

## Vuln Detail

```c
#define NODEDSZ(node) ((node)->mn_lo | ((unsigned)(node)->mn_hi << 16))
static void
mdb_node_del(MDB_cursor *mc, int ksize)
{
	MDB_page *mp = mc->mc_pg[mc->mc_top];
	indx_t	indx = mc->mc_ki[mc->mc_top];
	unsigned int	 sz;
	
	……
	node = NODEPTR(mp, indx);
	sz = NODESIZE + node->mn_ksize;
	if (IS_LEAF(mp)) {
		if (F_ISSET(node->mn_flags, F_BIGDATA))
			sz += sizeof(pgno_t);
		else
        //in normal condition,node->mn_hi=0,NODESZ(node)=node->mn_lo
	    //if node->mn_hi is modified to another value,e.g.0x8001,sz+=mn_lo|0x8001<<16
      	//the value of sz is very large
			sz += NODEDSZ(node); 
      		
	}
  	sz = EVEN(sz);
    ……
	base = (char *)mp + mp->mp_upper + PAGEBASE;
    //memmove doesn't check the value of dst,writing to an illegal address or a heap address
	memmove(base + sz, base, ptr - mp->mp_upper);
    ……
}
```

## Debug

```c
RAX  0x6067e568
 RBX  0x67d580 ◂— 0x3
 RCX  0x2
 RDX  0x18
 RDI  0x6067e568
 RSI  0x67e55c ◂— 0x1000000000003
 R8   0x1
 R9   0xff4
 R10  0x6000000c
 R11  0x7ffff7f4c3d0 ◂— 0x0
 R12  0x694480 ◂— 0x300000004
 R13  0x0
 R14  0x7fffffff9900 ◂— 0x1
 R15  0x67e574 ◂— 0x1000060000003
 RBP  0x6000000c
 RSP  0x7fffffff93e8 —▸ 0x7ffff5ca2b3e (mdb_node_del+222) ◂— sub    word ptr [rbx + 0xc], 2
 RIP  0x7ffff7751b48 (__memmove_avx_unaligned_erms+120) ◂— vmovdqu xmmword ptr [rdi], xmm0
───────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────
 ► 0x7ffff7751b48 <__memmove_avx_unaligned_erms+120>    vmovdqu xmmword ptr [rdi], xmm0
    ↓
   0x7ffff7751b53 <__memmove_avx_unaligned_erms+131>    mov    rcx, qword ptr [rsi + rdx - 8]
   0x7ffff7751b58 <__memmove_avx_unaligned_erms+136>    mov    rsi, qword ptr [rsi]
   0x7ffff7751b5b <__memmove_avx_unaligned_erms+139>    mov    qword ptr [rdi + rdx - 8], rcx
   0x7ffff7751b60 <__memmove_avx_unaligned_erms+144>    mov    qword ptr [rdi], rsi
   0x7ffff7751b63 <__memmove_avx_unaligned_erms+147>    ret    
 
   0x7ffff7751b64 <__memmove_avx_unaligned_erms+148>    mov    ecx, dword ptr [rsi + rdx - 4]
   0x7ffff7751b68 <__memmove_avx_unaligned_erms+152>    mov    esi, dword ptr [rsi]
   0x7ffff7751b6a <__memmove_avx_unaligned_erms+154>    mov    dword ptr [rdi + rdx - 4], ecx
   0x7ffff7751b6e <__memmove_avx_unaligned_erms+158>    mov    dword ptr [rdi], esi
   0x7ffff7751b70 <__memmove_avx_unaligned_erms+160>    ret    
───────────────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffff93e8 —▸ 0x7ffff5ca2b3e (mdb_node_del+222) ◂— sub    word ptr [rbx + 0xc], 2
01:0008│      0x7fffffff93f0 ◂— 0x0
02:0010│      0x7fffffff93f8 —▸ 0x7fffffff9540 ◂— 0x0
03:0018│      0x7fffffff9400 —▸ 0x7fffffff9910 ◂— 0x3
04:0020│      0x7fffffff9408 —▸ 0x7ffff5ca9586 (mdb_cursor_put+2326) ◂— mov    r15d, dword ptr [rsp]
05:0028│      0x7fffffff9410 ◂— 0x0
06:0030│      0x7fffffff9418 ◂— 0xf5cabbaf
07:0038│      0x7fffffff9420 ◂— 0x7fff00000000
─────────────────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────────────────
 ► f 0     7ffff7751b48 __memmove_avx_unaligned_erms+120
   f 1     7ffff5ca2b3e mdb_node_del+222
   f 2     7ffff5ca2b3e mdb_node_del+222
   f 3     7ffff5ca9586 mdb_cursor_put+2326
   f 4     7ffff5caba2b mdb_put+251
   f 5     7ffff5c9f300 trans_put+256
   f 6     7ffff70f41b3 PyEval_EvalFrameEx+28659
   f 7     7ffff7225278 PyEval_EvalCodeEx+2008
   f 8     7ffff70ed029 PyEval_EvalCode+25
   f 9           402ca1
   f 10           403087
Program received signal SIGSEGV (fault address 0x6067e568)
```

