- [Description](#description)
- [version](#version)
- [others](#others)
- [Test Target](#test-target)
- [1 vuln/H5O_fill_new_decode-heap-buffer-overflow](#1-vuln-h5o-fill-new-decode-heap-buffer-overflow)
  - [gdb info](#gdb-info)
  - [asan report](#asan-report)
- [2 vuln/H5O_layout_decode-heap-buffer-overflow](#2-vuln-h5o-layout-decode-heap-buffer-overflow)
  - [gdb info](#gdb-info)
  - [asan report](#asan-report)
- [3 vuln/H5O_pline_reset-out-of-bound-read](#3-vuln-h5o-pline-reset-out-of-bound-read)
  - [asan report](#asan-report)
- [4 vuln/H5T_copy-heap-buffer-overflow](#4-vuln-h5t-copy-heap-buffer-overflow)
- [5 vuln/H5VM_memcpyvv-heap-buffer-overflow](#5-vuln-h5vm-memcpyvv-heap-buffer-overflow)
  - [gdb info](#gdb-info)
  - [asan report](#asan-report)

## Description
HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data. HDF5 is portable and is extensible, allowing applications to evolve in their use of HDF5. The HDF5 Technology suite includes tools and applications for managing, manipulating, viewing, and analyzing data in the HDF5 format.
link: https://portal.hdfgroup.org/display/HDF5/HDF5
## version
h5dump: Version 1.8.20

## others
this bug is reported by pwd@360TeamSeri0us, 
please send email to   teamSeri0us360@gmail.com if you have some quetion.

## Test Target
./h5dump-shared $file


## 1 vuln/H5O_fill_new_decode-heap-buffer-overflow

### gdb info
```
───────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x7ffff641e010 ◂— 0x0
 RBX  0x5555557b9828 —▸ 0x7ffff7b7db80 (H5O_MSG_FILL_NEW) ◂— 0x5
 RCX  0x5555557b94e8 ◂— 0x100100003
 RDX  0x800000
*RDI  0x7ffff641e010 ◂— 0x0
 RSI  0x5555557b94e8 ◂— 0x100100003
 R8   0xffffffff
 R9   0x0
 R10  0x22
 R11  0x246
 R12  0x555555559d30 (_start) ◂— xor    ebp, ebp
 R13  0x7fffffffdc10 ◂— 0x2
 R14  0x0
 R15  0x0
 RBP  0x7fffffffcd60 —▸ 0x7fffffffcdb0 —▸ 0x7fffffffce20 —▸ 0x7fffffffce70 —▸ 0x7fffffffced0 ◂— ...
 RSP  0x7fffffffcd10 —▸ 0x5555557b9390 —▸ 0x7ffff7f57010 ◂— 0x5cac0e
*RIP  0x7ffff7746331 (H5O_fill_new_decode+751) ◂— call   0x7ffff75e6bb0
─────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────────────────────────────
   0x7ffff774631f <H5O_fill_new_decode+733>     mov    rax, qword ptr [rbp - 8]
   0x7ffff7746323 <H5O_fill_new_decode+737>     mov    rax, qword ptr [rax + 0x40]
   0x7ffff7746327 <H5O_fill_new_decode+741>     mov    rcx, qword ptr [rbp - 0x48]
   0x7ffff774632b <H5O_fill_new_decode+745>     mov    rsi, rcx
   0x7ffff774632e <H5O_fill_new_decode+748>     mov    rdi, rax
 ► 0x7ffff7746331 <H5O_fill_new_decode+751>     call   memcpy@plt <0x7ffff75e6bb0>
        dest: 0x7ffff641e010 ◂— 0x0
        src: 0x5555557b94e8 ◂— 0x100100003
        n: 0x800000
 
   0x7ffff7746336 <H5O_fill_new_decode+756>     jmp    H5O_fill_new_decode+1318 <0x7ffff7746568>
    ↓
   0x7ffff7746568 <H5O_fill_new_decode+1318>    mov    rax, qword ptr [rbp - 8]
   0x7ffff774656c <H5O_fill_new_decode+1322>    mov    qword ptr [rbp - 0x10], rax
   0x7ffff7746570 <H5O_fill_new_decode+1326>    cmp    qword ptr [rbp - 0x10], 0
   0x7ffff7746575 <H5O_fill_new_decode+1331>    jne    H5O_fill_new_decode+1395 <0x7ffff77465b5>
──────────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]──────────────────────────────────────────────────────────────────────────────────────────────
   217         if(fill->fill_defined) {
   218             INT32DECODE(p, fill->size);
   219             if(fill->size > 0) {
   220                 H5_CHECK_OVERFLOW(fill->size, ssize_t, size_t);
   221                 if(NULL == (fill->buf = H5MM_malloc((size_t)fill->size)))
 ► 222                     HGOTO_ERROR(H5E_RESOURCE, H5E_NOSPACE, NULL, "memory allocation failed for fill value")
   223                 HDmemcpy(fill->buf, p, (size_t)fill->size);
   224             } /* end if */
   225         } /* end if */
   226         else
   227             fill->size = (-1);
──────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffcd10 —▸ 0x5555557b9390 —▸ 0x7ffff7f57010 ◂— 0x5cac0e
01:0008│      0x7fffffffcd18 —▸ 0x5555557b94e8 ◂— 0x100100003
02:0010│      0x7fffffffcd20 —▸ 0x7fffffffcde4 ◂— 0x0
03:0018│      0x7fffffffcd28 —▸ 0x5555557b9390 —▸ 0x7ffff7f57010 ◂— 0x5cac0e
04:0020│      0x7fffffffcd30 ◂— 0xa00000800000001
05:0028│      0x7fffffffcd38 —▸ 0x5555557b65b0 —▸ 0x5555557b6f80 ◂— 0x482f6e6c75762f2e ('./vuln/H')
06:0030│      0x7fffffffcd40 —▸ 0x7fffffffce40 ◂— 0x50a000008
07:0038│      0x7fffffffcd48 ◂— 0x0
────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7746331 H5O_fill_new_decode+751
   f 1     7ffff77457d6 H5O_fill_new_shared_decode+260
   f 2     7ffff774ddbe H5O_msg_read_oh+498
   f 3     7ffff774dad7 H5O_msg_read+202
   f 4     7ffff7651ea5 H5D__open_oid+1326
   f 5     7ffff7651528 H5D_open+802
   f 6     7ffff762efd3 H5Dopen2+1196
   f 7     7ffff7bc8ea0 find_objs_cb+269
   f 8     7ffff7bc9c2c traverse_cb+698
   f 9     7ffff76c171e H5G_visit_cb+639
   f 10     7ffff76c968c H5G__node_iterate+661

```

### asan report
```
==3247==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==3247==Installed the sigaction for signal 11
==3247==Installed the sigaction for signal 7
==3247==Installed the sigaction for signal 8
==3247==T0: stack [0x7fff03063000,0x7fff03863000) size 0x800000; local=0x7fff03860be8
==3247==AddressSanitizer Init done
=================================================================
==3247==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6120000260d8 at pc 0x0000004dcd22 bp 0x7fff0385f130 sp 0x7fff0385e8e0
READ of size 8388608 at 0x6120000260d8 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7f9418855056 in H5O_fill_new_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Ofill.c:222:17
    #2 0x7f9418855056 in H5O_fill_new_shared_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Oshared.h:82
    #3 0x7f941886d0ba in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #4 0x7f941886c7d0 in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29
    #5 0x7f9418573142 in H5D__open_oid /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1395:20
    #6 0x7f9418573142 in H5D_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1256
    #7 0x7f9418504d7e in H5Dopen2 /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5D.c:366:24
    #8 0x7f94193739b0 in find_objs_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:505:28
    #9 0x7f941937c289 in traverse_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:219:16
    #10 0x7f94186cbcf7 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:937:17
    #11 0x7f94186e13f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #12 0x7f94184b2bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #13 0x7f94184b2602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #14 0x7f94186fa785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #15 0x7f94186eb37a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #16 0x7f94186cad32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #17 0x7f9418e5390c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #18 0x7f9419376e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #19 0x7f941937aba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #20 0x7f94193731c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #21 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #22 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #23 0x7f9417317b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #24 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x6120000260d8 is located 0 bytes to the right of 280-byte region [0x612000025fc0,0x6120000260d8)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7f9418e63758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c247fffcbc0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcbd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fffcbe0: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
  0x0c247fffcbf0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c247fffcc10: 00 00 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa
  0x0c247fffcc20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==3247==ABORTING

```


## 2 vuln/H5O_layout_decode-heap-buffer-overflow

### gdb info

```
0x00007ffff7748cac	184	                HDmemcpy(mesg->storage.u.compact.buf, p, mesg->storage.u.compact.size);
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x7ffff699e010 ◂— 0x0
 RBX  0x5555557b98d0 —▸ 0x7ffff7b7dcc0 (H5O_MSG_LAYOUT) ◂— 0x8
 RCX  0x5555557b952c ◂— 0x0
 RDX  0x280000
*RDI  0x7ffff699e010 ◂— 0x0
 RSI  0x5555557b952c ◂— 0x0
 R8   0xffffffff
 R9   0x0
 R10  0x22
 R11  0x246
 R12  0x555555559d30 (_start) ◂— xor    ebp, ebp
 R13  0x7fffffffdc10 ◂— 0x2
 R14  0x0
 R15  0x0
 RBP  0x7fffffffc380 —▸ 0x7fffffffc3f0 —▸ 0x7fffffffc7a0 —▸ 0x7fffffffc7f0 —▸ 0x7fffffffc840 ◂— ...
 RSP  0x7fffffffc320 ◂— 0x100060001
*RIP  0x7ffff7748cac (H5O_layout_decode+1428) ◂— call   0x7ffff75e6bb0
─────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────────────────────────────
   0x7ffff7748c97 <H5O_layout_decode+1407>    mov    rcx, qword ptr [rbp - 0x58]
   0x7ffff7748c9b <H5O_layout_decode+1411>    mov    rax, qword ptr [rbp - 8]
   0x7ffff7748c9f <H5O_layout_decode+1415>    mov    rax, qword ptr [rax + 0x2d0]
   0x7ffff7748ca6 <H5O_layout_decode+1422>    mov    rsi, rcx
   0x7ffff7748ca9 <H5O_layout_decode+1425>    mov    rdi, rax
 ► 0x7ffff7748cac <H5O_layout_decode+1428>    call   memcpy@plt <0x7ffff75e6bb0>
        dest: 0x7ffff699e010 ◂— 0x0
        src: 0x5555557b952c ◂— 0x0
        n: 0x280000
 
   0x7ffff7748cb1 <H5O_layout_decode+1433>    mov    rdx, qword ptr [rbp - 0x58]
   0x7ffff7748cb5 <H5O_layout_decode+1437>    mov    rax, qword ptr [rbp - 8]
   0x7ffff7748cb9 <H5O_layout_decode+1441>    mov    rax, qword ptr [rax + 0x2c8]
   0x7ffff7748cc0 <H5O_layout_decode+1448>    add    rax, rdx
   0x7ffff7748cc3 <H5O_layout_decode+1451>    mov    qword ptr [rbp - 0x58], rax
──────────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]──────────────────────────────────────────────────────────────────────────────────────────────
   179 
   180         if(mesg->type == H5D_COMPACT) {
   181             UINT32DECODE(p, mesg->storage.u.compact.size);
   182             if(mesg->storage.u.compact.size > 0) {
   183                 if(NULL == (mesg->storage.u.compact.buf = H5MM_malloc(mesg->storage.u.compact.size)))
 ► 184                     HGOTO_ERROR(H5E_RESOURCE, H5E_NOSPACE, NULL, "memory allocation failed for compact data buffer")
   185                 HDmemcpy(mesg->storage.u.compact.buf, p, mesg->storage.u.compact.size);
   186                 p += mesg->storage.u.compact.size;
   187             } /* end if */
   188         } /* end if */
   189     } /* end if */
──────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffc320 ◂— 0x100060001
01:0008│      0x7fffffffc328 —▸ 0x5555557b952c ◂— 0x0
02:0010│      0x7fffffffc330 —▸ 0x7fffffffc3b4 ◂— 0x300000000
03:0018│      0x7fffffffc338 —▸ 0x5555557b9390 —▸ 0x7ffff7f57010 ◂— 0x5cac0e
04:0020│      0x7fffffffc340 ◂— 0xa00000800000001
05:0028│      0x7fffffffc348 —▸ 0x5555557b65b0 —▸ 0x5555557b6f80 ◂— 0x482f6e6c75762f2e ('./vuln/H')
06:0030│      0x7fffffffc350 ◂— 0x200000
07:0038│      0x7fffffffc358 ◂— 0x100001
────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7748cac H5O_layout_decode+1428
   f 1     7ffff774ddbe H5O_msg_read_oh+498
   f 2     7ffff765b92d H5O__dset_bh_info+146
   f 3     7ffff771a996 H5O_get_info+1553
   f 4     7ffff76c4743 H5G_loc_info_cb+196
   f 5     7ffff76d71e4 H5G_traverse_real+1786
   f 6     7ffff76d81d7 H5G_traverse+693
   f 7     7ffff76c4838 H5G_loc_info+129
   f 8     7ffff77140e7 H5Oget_info_by_name+871
   f 9     7ffff7bc9b5f traverse_cb+493
   f 10     7ffff76c171e H5G_visit_cb+639

```

### asan report
```
==104114==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==104114==Installed the sigaction for signal 11
==104114==Installed the sigaction for signal 7
==104114==Installed the sigaction for signal 8
==104114==T0: stack [0x7ffc7109d000,0x7ffc7189d000) size 0x800000; local=0x7ffc7189a778
==104114==AddressSanitizer Init done
=================================================================
==104114==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6120000260d8 at pc 0x0000004dcd22 bp 0x7ffc71897e10 sp 0x7ffc718975c0
READ of size 2621440 at 0x6120000260d8 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7f9bdd5b9b39 in H5O_layout_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Olayout.c:184:17
    #2 0x7f9bdd5ca0ba in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #3 0x7f9bdd2ecec4 in H5O__dset_bh_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Doh.c:383:16
    #4 0x7f9bdd528e48 in H5O_get_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:2879:16
    #5 0x7f9bdd430c1c in H5G_loc_info_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:699:8
    #6 0x7f9bdd469514 in H5G_traverse_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:638:16
    #7 0x7f9bdd46624a in H5G_traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:858:8
    #8 0x7f9bdd430951 in H5G_loc_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:744:8
    #9 0x7f9bdd52737a in H5Oget_info_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:659:8
    #10 0x7f9bde0d8cfb in traverse_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:204:12
    #11 0x7f9bdd428cf7 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:937:17
    #12 0x7f9bdd43e3f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #13 0x7f9bdd20fbc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #14 0x7f9bdd20f602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #15 0x7f9bdd457785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #16 0x7f9bdd44837a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #17 0x7f9bdd427d32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #18 0x7f9bddbb090c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #19 0x7f9bde0d3e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #20 0x7f9bde0d7ba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #21 0x7f9bde0d01c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #22 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #23 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #24 0x7f9bdc074b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #25 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x6120000260d8 is located 0 bytes to the right of 280-byte region [0x612000025fc0,0x6120000260d8)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7f9bddbc0758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c247fffcbc0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcbd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fffcbe0: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
  0x0c247fffcbf0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c247fffcc10: 00 00 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa
  0x0c247fffcc20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==104114==ABORTING

```

## 3 vuln/H5O_pline_reset-out-of-bound-read

### asan report

```
==4992==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==4992==Installed the sigaction for signal 11
==4992==Installed the sigaction for signal 7
==4992==Installed the sigaction for signal 8
==4992==T0: stack [0x7ffe26509000,0x7ffe26d09000) size 0x800000; local=0x7ffe26d071c8
==4992==AddressSanitizer Init done
AddressSanitizer:DEADLYSIGNAL
=================================================================
==4992==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x7f240f30b14a bp 0x000000000000 sp 0x7ffe26d05da0 T0)
==4992==The signal is caused by a READ memory access.
==4992==Hint: address points to the zero page.
    #0 0x7f240f30b149 in H5O_pline_reset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Opline.c:502:29
    #1 0x7f240f30b149 in H5O_pline_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Opline.c:217
    #2 0x7f240f30b149 in H5O_pline_shared_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Oshared.h:82
    #3 0x7f240f2fd0ba in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #4 0x7f240f2fc7d0 in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29
    #5 0x7f240f127e8b in H5G_get_create_plist /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5G.c:591:20
    #6 0x7f240f1272af in H5Gget_create_plist /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5G.c:510:21
    #7 0x5268de in dump_group /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:792:20
    #8 0x51a276 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1547:17
    #9 0x7f240dda7b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #10 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Opline.c:502:29 in H5O_pline_reset
==4992==ABORTING

```

## 4 vuln/H5T_copy-heap-buffer-overflow

```
DF5 "crashes/id:000083,sig:11,src:000244,op:ext_AO,pos:1007" {
=================================================================
==12555==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x604000000e74 at pc 0x0000004dcd22 bp 0x7ffc0a8a9950 sp 0x7ffc0a8a9100
READ of size 150994980 at 0x604000000e74 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7ff815f3c339 in H5T_copy /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5T.c:3281:17
    #2 0x7ff815da0d15 in H5O_dtype_copy /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Odtype.c:1191:23
    #3 0x7ff815dd5543 in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:550:29
    #4 0x7ff815dd47d0 in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29
    #5 0x7ff815f6b0a9 in H5T_open_oid /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Tcommit.c:833:31
    #6 0x7ff815f6b0a9 in H5T_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Tcommit.c:718
    #7 0x7ff815f6a23d in H5Topen2 /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Tcommit.c:598:24
    #8 0x523bda in dump_all_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:367:23
    #9 0x7ff815c31b55 in H5G_iterate_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:780:29
    #10 0x7ff815c493f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #11 0x7ff815a1abc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #12 0x7ff815a1a602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #13 0x7ff815c62785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #14 0x7ff815c5337a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #15 0x7ff815c30eaa in H5G_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:841:21
    #16 0x7ff8163b8f7d in H5Literate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1180:21
    #17 0x5276e5 in dump_group /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c
    #18 0x51a276 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1547:17
    #19 0x7ff81487fb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #20 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x604000000e74 is located 0 bytes to the right of 36-byte region [0x604000000e50,0x604000000e74)
allocated by thread T0 here:
    #0 0x4de088 in calloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:97
    #1 0x7ff8163cb80d in H5MM_calloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:105:21
    #2 0x7ff815da0175 in H5O_dtype_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Odtype.c:1111:8
    #3 0x7ff815da0175 in H5O_dtype_shared_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Oshared.h:82
    #4 0x7ff815dd50ba in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #5 0x7ff815dd47d0 in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c087fff8170: fa fa 00 00 00 00 00 00 fa fa 00 00 00 00 00 00
  0x0c087fff8180: fa fa 00 00 00 00 00 00 fa fa 00 00 00 00 00 fa
  0x0c087fff8190: fa fa 00 00 00 00 00 fa fa fa 00 00 00 00 00 fa
  0x0c087fff81a0: fa fa 00 00 00 00 00 00 fa fa 00 00 00 00 00 00
  0x0c087fff81b0: fa fa fd fd fd fd fd fa fa fa fd fd fd fd fd fa
=>0x0c087fff81c0: fa fa 00 00 00 00 00 00 fa fa 00 00 00 00[04]fa
  0x0c087fff81d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff81e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff81f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8200: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8210: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==12555==ABORTING

```




## 5 vuln/H5VM_memcpyvv-heap-buffer-overflow

### gdb info
```
0x00007ffff790a38a	1667	            HDmemcpy(dst, src, tmp_dst_len);
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x7ffff7e56018 ◂— 0x0
 RBX  0x4
 RCX  0x5555557bc0b0 ◂— 0x4
 RDX  0x100000
 RDI  0x7ffff7e56018 ◂— 0x0
 RSI  0x5555557bc0b0 ◂— 0x4
 R8   0x7fffffff3f30 ◂— 0x0
 R9   0x5555557bc0b0 ◂— 0x4
 R10  0x7
 R11  0x7ffff790a0d5 (H5VM_memcpyvv) ◂— push   rbp
 R12  0x555555559d30 (_start) ◂— xor    ebp, ebp
 R13  0x7fffffffdc20 ◂— 0x2
 R14  0x0
 R15  0x0
 RBP  0x7fffffff3e50 —▸ 0x7fffffff3ec0 —▸ 0x7fffffff8030 —▸ 0x7fffffff9af0 —▸ 0x7fffffff9b40 ◂— ...
 RSP  0x7fffffff3dc0 —▸ 0x5555557bc0b0 ◂— 0x4
*RIP  0x7ffff790a38a (H5VM_memcpyvv+693) ◂— call   0x7ffff75e6bb0
─────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────────────────────────────
   0x7ffff790a378 <H5VM_memcpyvv+675>    mov    rdx, qword ptr [rbp - 0x30]
   0x7ffff790a37c <H5VM_memcpyvv+679>    mov    rcx, qword ptr [rbp - 0x58]
   0x7ffff790a380 <H5VM_memcpyvv+683>    mov    rax, qword ptr [rbp - 0x60]
   0x7ffff790a384 <H5VM_memcpyvv+687>    mov    rsi, rcx
   0x7ffff790a387 <H5VM_memcpyvv+690>    mov    rdi, rax
 ► 0x7ffff790a38a <H5VM_memcpyvv+693>    call   memcpy@plt <0x7ffff75e6bb0>
        dest: 0x7ffff7e56018 ◂— 0x0
        src: 0x5555557bc0b0 ◂— 0x4
        n: 0x100000
 
   0x7ffff790a38f <H5VM_memcpyvv+698>    mov    rax, qword ptr [rbp - 0x30]
   0x7ffff790a393 <H5VM_memcpyvv+702>    add    qword ptr [rbp - 0x20], rax
   0x7ffff790a397 <H5VM_memcpyvv+706>    add    qword ptr [rbp - 0x48], 8
   0x7ffff790a39c <H5VM_memcpyvv+711>    add    qword ptr [rbp - 0x50], 8
   0x7ffff790a3a1 <H5VM_memcpyvv+716>    mov    rax, qword ptr [rbp - 0x48]
──────────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]──────────────────────────────────────────────────────────────────────────────────────────────
   1662 
   1663             /* Update source pointer */
   1664             src += tmp_dst_len;
   1665 
   1666             /* Update destination information */
 ► 1667             dst_len_ptr++;
   1668             tmp_dst_len = *dst_len_ptr;
   1669             dst = (unsigned char *)_dst + *dst_off_ptr;
   1670         } while(tmp_dst_len < tmp_src_len);
   1671 
   1672         /* Roll accumulated sequence lengths into return value */
──────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffff3dc0 —▸ 0x5555557bc0b0 ◂— 0x4
01:0008│      0x7fffffff3dc8 —▸ 0x7fffffff3f30 ◂— 0x0
02:0010│      0x7fffffff3dd0 —▸ 0x7fffffff3f48 ◂— 0x100000
03:0018│      0x7fffffff3dd8 —▸ 0x7fffffff3f38 ◂— 0x0
04:0020│      0x7fffffff3de0 ◂— 0x1
05:0028│      0x7fffffff3de8 —▸ 0x7ffff7e56018 ◂— 0x0
... ↓
07:0038│      0x7fffffff3df8 —▸ 0x5555557bc0b0 ◂— 0x4
────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff790a38a H5VM_memcpyvv+693
   f 1     7ffff763224d H5D__compact_readvv+106
   f 2     7ffff765ca2e H5D__gather_file+884
   f 3     7ffff765d654 H5D__scatgath_read+748
   f 4     7ffff76458d5 H5D__contig_read+79
   f 5     7ffff765868b H5D__read+2568
   f 6     7ffff7656ea4 H5Dread+2886
   f 7     7ffff7bbb7e2 h5tools_dump_simple_dset+1727
   f 8     7ffff7bbc0fc h5tools_dump_dset+493
   f 9     7ffff7bc3769 h5tools_dump_data+1250
   f 10     555555561131 dump_dataset+1614

```

### asan report

```
HDF5 "crashes/id:000094,sig:11,src:000275,op:flip2,pos:1098" {
GROUP "/" {
   DATASET "dset1" {
      DATATYPE  H5T_STD_I32BE
      DATASPACE  SIMPLE { ( 8, 8, 8, 8, 1048590, 4049354197541335090, 55195500426545, 4297064456, 2147484417, 2048 ) / ( 34359738376, 4, 7340032, 0, 0, 0, 0, 0, 0, 0 ) }
=================================================================
==110070==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6020000052b8 at pc 0x0000004dcd22 bp 0x7ffc2ae4a470 sp 0x7ffc2ae49c20
READ of size 1048576 at 0x6020000052b8 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7f8921c9dde4 in H5VM_memcpyvv /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5VM.c:1667:13
    #2 0x7f89212e20e0 in H5D__compact_readvv /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dcompact.c:298:21
    #3 0x7f8921368d20 in H5D__gather_file /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dscatgath.c:249:12
    #4 0x7f892136679b in H5D__scatgath_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dscatgath.c:512:13
    #5 0x7f8921324268 in H5D__contig_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dcontig.c:540:8
    #6 0x7f89213581a3 in H5D__read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dio.c:604:8
    #7 0x7f8921355f72 in H5Dread /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dio.c:222:10
    #8 0x7f8922128191 in h5tools_dump_simple_dset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:1611:13
    #9 0x7f8922128191 in h5tools_dump_dset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:1786
    #10 0x7f8922136040 in h5tools_dump_data /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:3757:18
    #11 0x528ce2 in dump_dataset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:1064:21
    #12 0x52436c in dump_all_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:356:17
    #13 0x7f892149db55 in H5G_iterate_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:780:29
    #14 0x7f89214b53f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #15 0x7f8921286bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #16 0x7f8921286602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #17 0x7f89214ce785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #18 0x7f89214bf37a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #19 0x7f892149ceaa in H5G_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:841:21
    #20 0x7f8921c24f7d in H5Literate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1180:21
    #21 0x5276e5 in dump_group /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c
    #22 0x51a276 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1547:17
    #23 0x7f89200ebb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #24 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x6020000052b8 is located 0 bytes to the right of 8-byte region [0x6020000052b0,0x6020000052b8)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7f8921c37758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c047fff8a00: fa fa fd fa fa fa fd fa fa fa 00 07 fa fa 00 fa
  0x0c047fff8a10: fa fa 07 fa fa fa fd fa fa fa fd fa fa fa fd fa
  0x0c047fff8a20: fa fa 00 00 fa fa 04 fa fa fa fd fa fa fa fd fa
  0x0c047fff8a30: fa fa fd fd fa fa fd fd fa fa 06 fa fa fa 07 fa
  0x0c047fff8a40: fa fa fd fa fa fa fd fa fa fa fd fa fa fa fd fa
=>0x0c047fff8a50: fa fa 01 fa fa fa 00[fa]fa fa 00 fa fa fa 00 fa
  0x0c047fff8a60: fa fa 00 fa fa fa 00 fa fa fa 00 fa fa fa 00 fa
  0x0c047fff8a70: fa fa 00 fa fa fa 00 fa fa fa fd fa fa fa fd fd
  0x0c047fff8a80: fa fa fd fd fa fa 00 fa fa fa 00 00 fa fa 00 00
  0x0c047fff8a90: fa fa 00 00 fa fa 00 00 fa fa fa fa fa fa fa fa
  0x0c047fff8aa0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==110070==ABORTING

```
