# lmdb memcpy非法目的地址

## Description

```
An issue was discovered in py_lmdb 0.97.With a wrong value of mn_flags,memcpy in function mdb_xcursor_init1 in lib/mdb.c will write to an illegal address.
```

## Version

version <=0.97

https://github.com/jnwatson/py-lmdb

## Vuln Detail

In normal condition,the value of `mn_flags` is 0.With a wrong value of `mn_flags`,`mdb_xcursor_init1` function will be called.

```c
#define F_ISSET(w, f)	 (((w) & (f)) == (f))
#define F_DUPDATA	 0x04
static int
mdb_cursor_set(MDB_cursor *mc, MDB_val *key, MDB_val *data,
    MDB_cursor_op op, int *exactp){
  ……
//In normal conditon,mdb_xcursor_init1 won't be called since mn_flags=0
//with a value of 0xf,mdb_xcursor_init1 will be called
//PS：mc->mc_xcursor=0 at this time
if (F_ISSET(leaf->mn_flags, F_DUPDATA)) {
		mdb_xcursor_init1(mc, leaf);
	}
  ……
}
```

Memcpy in `mdb_xcursor_init1`  doesn't check the parameters.

```c
static void
mdb_xcursor_init1(MDB_cursor *mc, MDB_node *node)
{
	MDB_xcursor *mx = mc->mc_xcursor;//mx=0

	if (node->mn_flags & F_SUBDATA) {
		memcpy(&mx->mx_db, NODEDATA(node), sizeof(MDB_db));//dst is illegal
      
 }
```

## Debug

```C
RAX  0x67e571 ◂— 0x3646464
 RBX  0x7fffffff9540 ◂— 0x0
 RCX  0x0
 RDX  0x67e568 ◂— 0x1000f00000003
 RDI  0x0
 RSI  0x7fffffff9568 —▸ 0x694638 ◂— 0x1000000000000
 R8   0x0
 R9   0x0
 R10  0xffffffff
 R11  0x7ffff7f4c3d0 ◂— 0x0
 R12  0x7fffffff9900 ◂— 0x1
 R13  0xf
 R14  0x7fffffff9490 ◂— 0x1
 R15  0x67e568 ◂— 0x1000f00000003
 RBP  0x67d580 ◂— 0x3
 RSP  0x7fffffff9388 —▸ 0x7ffff5ca5080 (mdb_cursor_set+768) ◂— cmp    qword ptr [rsp + 8], 0
 RIP  0x7ffff5ca16b4 (mdb_xcursor_init1.isra+244) ◂— movups xmmword ptr [rdi + 0x188], xmm0
───────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────
   0x7ffff5ca15c0 <mdb_xcursor_init1.isra>        movzx  eax, word ptr [rdx + 6]
   0x7ffff5ca15c4 <mdb_xcursor_init1.isra+4>      test   byte ptr [rdx + 4], 2
   0x7ffff5ca15c8 <mdb_xcursor_init1.isra+8>      lea    rax, [rdx + rax + 8]
   0x7ffff5ca15cd <mdb_xcursor_init1.isra+13>     jne    mdb_xcursor_init1.isra+240 <0x7ffff5ca16b0>
    ↓
   0x7ffff5ca16b0 <mdb_xcursor_init1.isra+240>    movdqu xmm0, xmmword ptr [rax]
 ► 0x7ffff5ca16b4 <mdb_xcursor_init1.isra+244>    movups xmmword ptr [rdi + 0x188], xmm0
   0x7ffff5ca16bb <mdb_xcursor_init1.isra+251>    movdqu xmm0, xmmword ptr [rax + 0x10]
   0x7ffff5ca16c0 <mdb_xcursor_init1.isra+256>    movups xmmword ptr [rdi + 0x198], xmm0
   0x7ffff5ca16c7 <mdb_xcursor_init1.isra+263>    movdqu xmm0, xmmword ptr [rax + 0x20]
   0x7ffff5ca16cc <mdb_xcursor_init1.isra+268>    movabs rax, 0x400000000
   0x7ffff5ca16d6 <mdb_xcursor_init1.isra+278>    mov    qword ptr [rdi + 0x40], rax
───────────────────────────────────────────────────────[ SOURCE (CODE) ]────────────────────────────────────────────────────────
In file: /usr/include/x86_64-linux-gnu/bits/string_fortified.h
   29 
   30 __fortify_function void *
   31 __NTH (memcpy (void *__restrict __dest, const void *__restrict __src,
   32 	       size_t __len))
   33 {
 ► 34   return __builtin___memcpy_chk (__dest, __src, __len, __bos0 (__dest));
   35 }
   36 
   37 __fortify_function void *
   38 __NTH (memmove (void *__dest, const void *__src, size_t __len))
   39 {
───────────────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffff9388 —▸ 0x7ffff5ca5080 (mdb_cursor_set+768) ◂— cmp    qword ptr [rsp + 8], 0
01:0008│      0x7fffffff9390 ◂— 0x0
02:0010│      0x7fffffff9398 —▸ 0x7fffffff94a0 ◂— 0x3
03:0018│      0x7fffffff93a0 ◂— 0x0
04:0020│      0x7fffffff93a8 —▸ 0x694580 ◂— 0x0
05:0028│      0x7fffffff93b0 —▸ 0x7ffff7f1a2e8 —▸ 0x7ffff7580b00 (_Py_NoneStruct) ◂— 0x64e
06:0030│      0x7fffffff93b8 ◂— 0x1
07:0038│      0x7fffffff93c0 ◂— 0x0
─────────────────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────────────────
 ► f 0     7ffff5ca16b4 mdb_xcursor_init1.isra+244
   f 1     7ffff5ca16b4 mdb_xcursor_init1.isra+244
   f 2     7ffff5ca5080 mdb_cursor_set+768
   f 3     7ffff5ca8f98 mdb_cursor_put+808
   f 4     7ffff5caba2b mdb_put+251
   f 5     7ffff5c9f300 trans_put+256
   f 6     7ffff70f41b3 PyEval_EvalFrameEx+28659
   f 7     7ffff7225278 PyEval_EvalCodeEx+2008
   f 8     7ffff70ed029 PyEval_EvalCode+25
   f 9           402ca1
   f 10           403087
Program received signal SIGSEGV (fault address 0x188)
pwndbg> bt
#0  0x00007ffff5ca16b4 in memcpy (__len=48, __src=0x67e571, __dest=0x188) at /usr/include/x86_64-linux-gnu/bits/string_fortified.h:34
#1  mdb_xcursor_init1 (node=node@entry=0x67e568, mc=<optimized out>, mc=<optimized out>) at lib/mdb.c:7500
#2  0x00007ffff5ca5080 in mdb_cursor_set (mc=mc@entry=0x7fffffff9540, key=key@entry=0x7fffffff9900, data=0x7fffffff94a0, op=op@entry=MDB_SET, exactp=exactp@entry=0x7fffffff9490) at lib/mdb.c:6142
#3  0x00007ffff5ca8f98 in mdb_cursor_put (mc=0x7fffffff9540, key=0x7fffffff9900, data=0x7fffffff9910, flags=0) at lib/mdb.c:6583
#4  0x00007ffff5caba2b in mdb_put (txn=0x694580, dbi=1, key=key@entry=0x7fffffff9900, data=data@entry=0x7fffffff9910, flags=flags@entry=0) at lib/mdb.c:8991
#5  0x00007ffff5c9f300 in trans_put (self=0x7ffff7f488f0, args=<optimized out>, kwds=<optimized out>) at lmdb/cpython.c:3291
#6  0x00007ffff70f41b3 in PyEval_EvalFrameEx () from /tmp/_MEIoP7vm2/libpython2.7.so.1.0
#7  0x00007ffff7225278 in PyEval_EvalCodeEx () from /tmp/_MEIoP7vm2/libpython2.7.so.1.0
#8  0x00007ffff70ed029 in PyEval_EvalCode () from /tmp/_MEIoP7vm2/libpython2.7.so.1.0
#9  0x0000000000402ca1 in ?? ()
#10 0x0000000000403087 in ?? ()
#11 0x00007ffff75e4b97 in __libc_start_main (main=0x401a70, argc=1, argv=0x7fffffffdcb8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdca8) at ../csu/libc-start.c:310
#12 0x0000000000401a9e in ?? ()
```
## others
```
please send email to teamseri0us360@gmail.com if you have any questions.
```
