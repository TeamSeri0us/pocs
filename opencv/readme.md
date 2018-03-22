
bugs of opencv
==================
** This work done with 360 TeamSerious **

# 1. out-of-bound write in FillColorRow4

An out of bound write error occurs when reads it by using cv::imread.

```
==14475== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==14475== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==14475== Command: ./gtest.elf ../../../fuzz-tests/GaussianBlur-test/out/crashes/id:000001,sig:06,src:000001,op:flip1,pos:21
==14475==
==14475== Warning: set address range perms: large range [0x3a044040, 0xfa044c88) (undefined)
==14475== Invalid write of size 4
==14475==    at 0x514CBC3: FillColorRow4(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:496)
==14475==    by 0x5169284: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:251)
==14475==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==14475==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==14475==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==14475==  Address 0xfffffffff4044c20 is not stack'd, malloc'd or (recently) free'd
==14475==
==14475==
==14475== Process terminating with default action of signal 11 (SIGSEGV)
==14475==  Access not within mapped region at address 0xFFFFFFFFF4044C20
==14475==    at 0x514CBC3: FillColorRow4(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:496)
==14475==    by 0x5169284: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:251)
==14475==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==14475==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==14475==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==14475==  If you believe this happened as a result of a stack
==14475==  overflow in your program's main thread (unlikely but
==14475==  possible), you can try to increase the size of the
==14475==  main thread stack using the --main-stacksize= flag.
==14475==  The main thread stack size used in this run was 8388608.
==14475==
==14475== HEAP SUMMARY:
==14475==     in use at exit: 3,238,103,506 bytes in 397 blocks
==14475==   total heap usage: 458 allocs, 61 frees, 3,238,113,514 bytes allocated
==14475==
==14475== LEAK SUMMARY:
==14475==    definitely lost: 0 bytes in 0 blocks
==14475==    indirectly lost: 0 bytes in 0 blocks
==14475==      possibly lost: 3,221,236,783 bytes in 114 blocks
==14475==    still reachable: 16,866,723 bytes in 283 blocks
==14475==         suppressed: 0 bytes in 0 blocks
==14475== Rerun with --leak-check=full to see details of leaked memory
==14475==
==14475== For counts of detected and suppressed errors, rerun with: -v
==14475== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault

```

# 2. A heap-based buf overflow results to invalid write in fseek.

```
==25260== Memcheck, a memory error detector
==25260== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==25260== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==25260== Command: ./gtest.elf ../../../fuzz-tests/GaussianBlur-test/out/crashes/id:000002,sig:06,src:000001,op:flip1,pos:47
==25260==
==25260== Invalid write of size 2
==25260==    at 0x4C2F7E3: memcpy@@GLIBC_2.14 (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==25260==    by 0x5178F29: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:235)
==25260==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==25260==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==25260==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==25260==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==25260==  Address 0xecb66c0 is 0 bytes after a block of size 1,264 alloc'd
==25260==    at 0x4C2B0E0: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==25260==    by 0x513AD5C: cv::Ptr<cv::BmpDecoder> cv::makePtr<cv::BmpDecoder>() (ptr.inl.hpp:301)
==25260==    by 0x5167CE3: cv::BmpDecoder::newDecoder() const (grfmt_bmp.cpp:76)
==25260==    by 0x51322DB: cv::findDecoder(cv::String const&) (loadsave.cpp:199)
==25260==    by 0x5134301: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:384)
==25260==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==25260==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==25260==
==25260== Source and destination overlap in memcpy(0xecb676a, 0xecb67f0, 632)
==25260==    at 0x4C2F71C: memcpy@@GLIBC_2.14 (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==25260==    by 0x5178F29: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:235)
==25260==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==25260==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==25260==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==25260==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==25260==
==25260== Invalid read of size 8
==25260==    at 0x74928F5: fseek (fseek.c:38)
==25260==    by 0x51784A6: cv::RBaseStream::readBlock() (bitstrm.cpp:104)
==25260==    by 0x5178F9E: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:233)
==25260==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==25260==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==25260==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==25260==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==25260==  Address 0x33333333333303b is not stack'd, malloc'd or (recently) free'd
==25260==
==25260==
==25260== Process terminating with default action of signal 11 (SIGSEGV)
==25260==  General Protection Fault
==25260==    at 0x74928F5: fseek (fseek.c:38)
==25260==    by 0x51784A6: cv::RBaseStream::readBlock() (bitstrm.cpp:104)
==25260==    by 0x5178F9E: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:233)
==25260==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==25260==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==25260==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==25260==    by 0x400DFA: main (33_GaussianBlur.cpp:34)
==25260== Invalid read of size 8
==25260==    at 0x749CF52: _IO_flush_all_lockp (genops.c:844)
==25260==    by 0x749D0C9: _IO_cleanup (genops.c:1013)
==25260==    by 0x7589DBA: __libc_freeres (in /lib/x86_64-linux-gnu/libc-2.19.so)
==25260==    by 0x4A256BC: _vgnU_freeres (in /usr/lib/valgrind/vgpreload_core-amd64-linux.so)
==25260==    by 0xFFF0002DF: ???
==25260==  Address 0x3311110000030018 is not stack'd, malloc'd or (recently) free'd
==25260==
==25260==
==25260== Process terminating with default action of signal 11 (SIGSEGV)
==25260==  General Protection Fault
==25260==    at 0x749CF52: _IO_flush_all_lockp (genops.c:844)
==25260==    by 0x749D0C9: _IO_cleanup (genops.c:1013)
==25260==    by 0x7589DBA: __libc_freeres (in /lib/x86_64-linux-gnu/libc-2.19.so)
==25260==    by 0x4A256BC: _vgnU_freeres (in /usr/lib/valgrind/vgpreload_core-amd64-linux.so)
==25260==    by 0xFFF0002DF: ???
==25260==
==25260== HEAP SUMMARY:
==25260==     in use at exit: 97,530 bytes in 393 blocks
==25260==   total heap usage: 454 allocs, 61 frees, 107,538 bytes allocated
==25260==
==25260== LEAK SUMMARY:
==25260==    definitely lost: 0 bytes in 0 blocks
==25260==    indirectly lost: 0 bytes in 0 blocks
==25260==      possibly lost: 8,167 bytes in 113 blocks
==25260==    still reachable: 89,363 bytes in 280 blocks
==25260==         suppressed: 0 bytes in 0 blocks
==25260== Rerun with --leak-check=full to see details of leaked memory
==25260==
==25260== For counts of detected and suppressed errors, rerun with: -v
==25260== ERROR SUMMARY: 260 errors from 4 contexts (suppressed: 0 from 0)
Segmentation fault
```

# 3. out-of-bound write in FillColorRow8

```
==15589== Memcheck, a memory error detector
==15589== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.==15589== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==15589== Command: ./opencv_test.elf ../../../fuzz-tests/medianBlur-test/out/crashes/id:000017,sig:06,src:000083,op:flip1,pos:21
==15589== 
==15589== Warning: set address range perms: large range [0x3a044040, 0xfa044c88) (undefined)==15589== Invalid write of size 4
==15589==    at 0x514CA25: FillColorRow8(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:470)
==15589==    by 0x5169A00: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:339)
==15589==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==15589==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==15589==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==15589==  Address 0xfffffffff4044c20 is not stack'd, malloc'd or (recently) free'd
==15589== 
==15589== 
==15589== Process terminating with default action of signal 11 (SIGSEGV)
==15589==  Access not within mapped region at address 0xFFFFFFFFF4044C20
==15589==    at 0x514CA25: FillColorRow8(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:470)
==15589==    by 0x5169A00: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:339)
==15589==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==15589==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==15589==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==15589==  If you believe this happened as a result of a stack
==15589==  overflow in your program's main thread (unlikely but
==15589==  possible), you can try to increase the size of the
==15589==  main thread stack using the --main-stacksize= flag.
==15589==  The main thread stack size used in this run was 8388608.
==15589== 
==15589== HEAP SUMMARY:
==15589==     in use at exit: 3,254,880,734 bytes in 397 blocks
==15589==   total heap usage: 458 allocs, 61 frees, 3,254,890,742 bytes allocated
==15589== 
==15589== LEAK SUMMARY:
==15589==    definitely lost: 0 bytes in 0 blocks
==15589==    indirectly lost: 0 bytes in 0 blocks
==15589==      possibly lost: 3,221,236,779 bytes in 114 blocks
==15589==    still reachable: 33,643,955 bytes in 283 blocks
==15589==         suppressed: 0 bytes in 0 blocks
==15589== Rerun with --leak-check=full to see details of leaked memory
==15589== 
==15589== For counts of detected and suppressed errors, rerun with: -v
==15589== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault

```

# 4. buffer overflow  in cv::BmpDecoder::readData (memcpy)

```
Stopped reason: SIGSEGV
[----------------------------------registers-----------------------------------]
RAX: 0xffffffffc0000060 
RBX: 0x0 
RCX: 0x1850 
RDX: 0xffffffffc0000060 
RSI: 0x7fffffffd7b0 ('3' <repeats 21 times>)
RDI: 0x7fe82df73be0 ('3' <repeats 21 times>)
RBP: 0x7fffffffe310 --> 0x0 
RSP: 0x7fffffffd5e8 --> 0x7ffff763e62d (<cv::BmpDecoder::readData(cv::Mat&)+6797>:      mov    rax,QWORD PTR [rip+0x511044]        # 0x7ffff7b4f678 <__gcov0._ZN2cv10BmpDecoder8readDataERNS_3MatE+1176>)
RIP: 0x7ffff54c1ba4 (<__memcpy_sse2_unaligned+372>:     movdqu xmm8,XMMWORD PTR [rsi+rcx*1])
R8 : 0x185 
R9 : 0xffffffffc000006 
R10: 0x7fffffffd3b0 --> 0x0 
R11: 0x7ffff7603320 (<cv::Mat::channels() const>:       sub    rsp,0x8)
R12: 0x400c40 (<_start>:        xor    ebp,ebp)
R13: 0x7fffffffe3f0 --> 0x2 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff54c1b99 <__memcpy_sse2_unaligned+361>:        je     0x7ffff54c1c32 <__memcpy_sse2_unaligned+514>
   0x7ffff54c1b9f <__memcpy_sse2_unaligned+367>:        xor    ecx,ecx
   0x7ffff54c1ba1 <__memcpy_sse2_unaligned+369>:        xor    r8d,r8d
=> 0x7ffff54c1ba4 <__memcpy_sse2_unaligned+372>:        movdqu xmm8,XMMWORD PTR [rsi+rcx*1]
   0x7ffff54c1baa <__memcpy_sse2_unaligned+378>:        add    r8,0x1
   0x7ffff54c1bae <__memcpy_sse2_unaligned+382>:        movdqu XMMWORD PTR [rdi+rcx*1],xmm8
   0x7ffff54c1bb4 <__memcpy_sse2_unaligned+388>:        add    rcx,0x10
   0x7ffff54c1bb8 <__memcpy_sse2_unaligned+392>:        cmp    r9,r8
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffd5e8 --> 0x7ffff763e62d (<cv::BmpDecoder::readData(cv::Mat&)+6797>:     mov    rax,QWORD PTR [rip+0x511044]        # 0x7ffff7b4f678 <__gcov0._ZN2cv10BmpDecoder8readDataERNS_3MatE+1176>)
0008| 0x7fffffffd5f0 --> 0x1201204800000001 
0016| 0x7fffffffd5f8 --> 0x7ffff7fe2158 --> 0x7ffff149c000 --> 0x10102464c457f 
0024| 0x7fffffffd600 --> 0x7fffffffe240 --> 0x242ff4010 
0032| 0x7fffffffd608 --> 0x6150a0 --> 0x7ffff7a9ce50 --> 0x7ffff763bb24 (<cv::BmpDecoder::~BmpDecoder()>:       push   rbx)
0040| 0x7fffffffd610 --> 0x7ffff4de7cb0 --> 0x1 
0048| 0x7fffffffd618 --> 0x1007ffff7de7ea5 
0056| 0x7fffffffd620 --> 0x7ffff7feb4e8 --> 0x7ffff5427000 --> 0x10102464c457f 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
__memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:116
116     ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S: No such file or directory.
gdb-peda$ bt
#0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:116
#1  0x00007ffff763e62d in cv::BmpDecoder::readData (this=0x6150a0, img=...) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/grfmt_bmp.cpp:463
#2  0x00007ffff7608a8c in cv::imread_ (filename=..., flags=0x1, hdrtype=0x2, mat=0x7fffffffe240) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/loadsave.cpp:454
#3  0x00007ffff7609742 in cv::imread (filename=..., flags=0x1) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/loadsave.cpp:565
#4  0x0000000000400d91 in main ()
#5  0x00007ffff5448f45 in __libc_start_main (main=0x400d2d <main>, argc=0x2, argv=0x7fffffffe3f8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe3e8) at libc-start.c:287
#6  0x0000000000400c69 in _start ()
gdb-peda$ 

```

# 5. out-of-bound write in FillColorRow1

```
==21776== Memcheck, a memory error detector
==21776== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==21776== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==21776== Command: ./opencv_test.elf ../../../fuzz-tests/medianBlur-test/out/crashes/id:000023,sig:06,src:000185,op:ext_AO,pos:23
==21776== 
==21776== Warning: set address range perms: large range [0x3a044040, 0xe5f690a8) (undefined)
==21776== Invalid write of size 4
==21776==    at 0x514CED2: FillColorRow1(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:543)
==21776==    by 0x51690BC: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:236)
==21776==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==21776==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==21776==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==21776==  Address 0xffffffffe5f68fd7 is not stack'd, malloc'd or (recently) free'd
==21776== 
==21776== 
==21776== Process terminating with default action of signal 11 (SIGSEGV)
==21776==  Access not within mapped region at address 0xFFFFFFFFE5F68FD7
==21776==    at 0x514CED2: FillColorRow1(unsigned char*, unsigned char*, int, PaletteEntry*) (utils.cpp:543)
==21776==    by 0x51690BC: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:236)
==21776==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==21776==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==21776==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==21776==  If you believe this happened as a result of a stack
==21776==  overflow in your program's main thread (unlikely but
==21776==  possible), you can try to increase the size of the
==21776==  main thread stack using the --main-stacksize= flag.
==21776==  The main thread stack size used in this run was 8388608.
==21776== 
==21776== HEAP SUMMARY:
==21776==     in use at exit: 2,884,881,858 bytes in 396 blocks
==21776==   total heap usage: 457 allocs, 61 frees, 2,884,891,866 bytes allocated
==21776== 
==21776== LEAK SUMMARY:
==21776==    definitely lost: 0 bytes in 0 blocks
==21776==    indirectly lost: 0 bytes in 0 blocks
==21776==      possibly lost: 2,884,792,399 bytes in 114 blocks
==21776==    still reachable: 89,459 bytes in 282 blocks
==21776==         suppressed: 0 bytes in 0 blocks
==21776== Rerun with --leak-check=full to see details of leaked memory
==21776== 
==21776== For counts of detected and suppressed errors, rerun with: -v
==21776== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault

```

# 6. out-of-bound write in readData

```
==24457== Memcheck, a memory error detector==24457== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==24457== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==24457== Command: ./opencv_test.elf ../../../fuzz-tests/medianBlur-test/out/crashes/id:000027,sig:06,src:000302,op:flip1,pos:21
==24457== 
==24457== Warning: set address range perms: large range [0x3a044040, 0xfa0459a8) (undefined)
==24457== Invalid write of size 1
==24457==    at 0x516949C: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:283)
==24457==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==24457==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==24457==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==24457==  Address 0xfffffffff40458d7 is not stack'd, malloc'd or (recently) free'd
==24457== 
==24457== 
==24457== Process terminating with default action of signal 11 (SIGSEGV)
==24457==  Access not within mapped region at address 0xFFFFFFFFF40458D7
==24457==    at 0x516949C: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:283)
==24457==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==24457==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==24457==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==24457==  If you believe this happened as a result of a stack
==24457==  overflow in your program's main thread (unlikely but
==24457==  possible), you can try to increase the size of the
==24457==  main thread stack using the --main-stacksize= flag.
==24457==  The main thread stack size used in this run was 8388608.
==24457== 
==24457== HEAP SUMMARY:
==24457==     in use at exit: 3,238,106,882 bytes in 397 blocks
==24457==   total heap usage: 458 allocs, 61 frees, 3,238,116,890 bytes allocated
==24457== 
==24457== LEAK SUMMARY:
==24457==    definitely lost: 0 bytes in 0 blocks
==24457==    indirectly lost: 0 bytes in 0 blocks
==24457==      possibly lost: 3,221,240,139 bytes in 114 blocks
==24457==    still reachable: 16,866,743 bytes in 283 blocks
==24457==         suppressed: 0 bytes in 0 blocks
==24457== Rerun with --leak-check=full to see details of leaked memory
==24457== 
==24457== For counts of detected and suppressed errors, rerun with: -v
==24457== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault

```

# 7. out of bound write in FillUniColor
```
==10897== Memcheck, a memory error detector
==10897== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==10897== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==10897== Command: ./opencv_test.elf ../../../fuzz-tests/medianBlur-test/out/crashes/id:000032,sig:06,src:000516,op:flip1,pos:21
==10897== 
==10897== Warning: set address range perms: large range [0x3a044040, 0xfa0459a8) (undefined)
==10897== Invalid write of size 1
==10897==    at 0x514C749: FillUniColor(unsigned char*, unsigned char*&, int, int, int&, int, int, PaletteEntry) (utils.cpp:417)
==10897==    by 0x5169824: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:315)
==10897==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==10897==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==10897==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==10897==  Address 0xfffffffff40458d7 is not stack'd, malloc'd or (recently) free'd
==10897== 
==10897== 
==10897== Process terminating with default action of signal 11 (SIGSEGV)
==10897==  Access not within mapped region at address 0xFFFFFFFFF40458D7
==10897==    at 0x514C749: FillUniColor(unsigned char*, unsigned char*&, int, int, int&, int, int, PaletteEntry) (utils.cpp:417)
==10897==    by 0x5169824: cv::BmpDecoder::readData(cv::Mat&) (grfmt_bmp.cpp:315)
==10897==    by 0x5134A8B: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:454)
==10897==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==10897==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==10897==  If you believe this happened as a result of a stack
==10897==  overflow in your program's main thread (unlikely but
==10897==  possible), you can try to increase the size of the
==10897==  main thread stack using the --main-stacksize= flag.
==10897==  The main thread stack size used in this run was 8388608.
==10897== 
==10897== HEAP SUMMARY:
==10897==     in use at exit: 3,238,106,882 bytes in 397 blocks
==10897==   total heap usage: 458 allocs, 61 frees, 3,238,116,890 bytes allocated
==10897== 
==10897== LEAK SUMMARY:
==10897==    definitely lost: 0 bytes in 0 blocks
==10897==    indirectly lost: 0 bytes in 0 blocks
==10897==      possibly lost: 3,221,240,139 bytes in 114 blocks
==10897==    still reachable: 16,866,743 bytes in 283 blocks
==10897==         suppressed: 0 bytes in 0 blocks
==10897== Rerun with --leak-check=full to see details of leaked memory
==10897== 
==10897== For counts of detected and suppressed errors, rerun with: -v
==10897== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault

```


# 8. Invalid read in fread
```
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
[----------------------------------registers-----------------------------------]
RAX: 0x7ffff54a0210 (<__GI__IO_file_xsgetn>:    push   r14)
RBX: 0x61d5b0 --> 0xc00002574442 
RCX: 0xfffffff9 
RDX: 0x28 ('(')
RSI: 0x7ffff7ff3fd1 
RDI: 0x6155a0 --> 0xc00002574d42 
RBP: 0x2f ('/')
RSP: 0x7fffffffdbc8 --> 0x7ffff54a038e (<__GI__IO_file_xsgetn+382>:     add    QWORD PTR [rbx+0x8],rbp)
RIP: 0x7ffff54b3ab0 (<__mempcpy_sse2+144>:      movzx  eax,BYTE PTR [rsi])
R8 : 0x61d690 --> 0x100000001 
R9 : 0x6155a0 --> 0xc00002574d42 
R10: 0x0 
R11: 0x246 
R12: 0x7fd1 
R13: 0x8000 
R14: 0x6155a0 --> 0xc00002574d42 
R15: 0x0
EFLAGS: 0x10297 (CARRY PARITY ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff54b3aa7 <__mempcpy_sse2+135>: lea    rdx,[rcx+rdx*1-0x8]
   0x7ffff54b3aac <__mempcpy_sse2+140>: sub    ecx,0x8
   0x7ffff54b3aaf <__mempcpy_sse2+143>: nop
=> 0x7ffff54b3ab0 <__mempcpy_sse2+144>: movzx  eax,BYTE PTR [rsi]
   0x7ffff54b3ab3 <__mempcpy_sse2+147>: mov    BYTE PTR [rdi],al
   0x7ffff54b3ab5 <__mempcpy_sse2+149>: inc    ecx
   0x7ffff54b3ab7 <__mempcpy_sse2+151>: lea    rsi,[rsi+0x1]
   0x7ffff54b3abb <__mempcpy_sse2+155>: lea    rdi,[rdi+0x1]
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdbc8 --> 0x7ffff54a038e (<__GI__IO_file_xsgetn+382>:    add    QWORD PTR [rbx+0x8],rbp)
0008| 0x7fffffffdbd0 --> 0x61d5b0 --> 0xc00002574442 
0016| 0x7fffffffdbd8 --> 0x8000 
0024| 0x7fffffffdbe0 --> 0x1 
0032| 0x7fffffffdbe8 --> 0x8000 
0040| 0x7fffffffdbf0 --> 0x0 
0048| 0x7fffffffdbf8 --> 0x7ffff549586f (<__GI__IO_fread+143>:  test   DWORD PTR [rbx],0x8000)
0056| 0x7fffffffdc00 --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
__mempcpy_sse2 () at ../sysdeps/x86_64/memcpy.S:166
166     ../sysdeps/x86_64/memcpy.S: No such file or directory.
gdb-peda$ bt
#0  __mempcpy_sse2 () at ../sysdeps/x86_64/memcpy.S:166
#1  0x00007ffff54a038e in __GI__IO_file_xsgetn (fp=0x61d5b0, data=<optimized out>, n=0x8000) at fileops.c:1396
#2  0x00007ffff549586f in __GI__IO_fread (buf=<optimized out>, size=0x1, count=0x8000, fp=0x61d5b0) at iofread.c:42
#3  0x00007ffff764c4e3 in cv::RBaseStream::readBlock (this=0x615140) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/bitstrm.cpp:105
#4  0x00007ffff764cf9f in cv::RLByteStream::getBytes (this=0x615140, buffer=0x615180, count=0x5d34843e) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/bitstrm.cpp:233
#5  0x00007ffff763c3b9 in cv::BmpDecoder::readHeader (this=0x6150a0) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/grfmt_bmp.cpp:122
#6  0x00007ffff7608549 in cv::imread_ (filename=..., flags=0x1, hdrtype=0x2, mat=0x7fffffffe240) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/loadsave.cpp:412
#7  0x00007ffff7609742 in cv::imread (filename=..., flags=0x1) at /data/xqx/tests/opencv-test/opencv/modules/imgcodecs/src/loadsave.cpp:565
#8  0x0000000000400d91 in main ()
#9  0x00007ffff5448f45 in __libc_start_main (main=0x400d2d <main>, argc=0x2, argv=0x7fffffffe3f8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe3e8) at libc-start.c:287
#10 0x0000000000400c69 in _start ()

```

```
==4831== Memcheck, a memory error detector
==4831== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4831== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==4831== Command: ./opencv_test.elf ../../../fuzz-tests/medianBlur-test/out/crashes/id:000040,sig:06,src:000820,op:havoc,rep:4
==4831== 
==4831== Invalid write of size 2
==4831==    at 0x4C2F7E3: memcpy@@GLIBC_2.14 (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==4831==    by 0x5178F29: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:235)
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==4831==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831==  Address 0xecb66c0 is 0 bytes after a block of size 1,264 alloc'd
==4831==    at 0x4C2B0E0: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==4831==    by 0x513AD5C: cv::Ptr<cv::BmpDecoder> cv::makePtr<cv::BmpDecoder>() (ptr.inl.hpp:301)
==4831==    by 0x5167CE3: cv::BmpDecoder::newDecoder() const (grfmt_bmp.cpp:76)
==4831==    by 0x51322DB: cv::findDecoder(cv::String const&) (loadsave.cpp:199)
==4831==    by 0x5134301: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:384)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831== 
==4831== Invalid write of size 1
==4831==    at 0x4C2F953: memcpy@@GLIBC_2.14 (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==4831==    by 0x5178F29: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:235)
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==4831==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831==  Address 0xecb66e8 is 24 bytes before a block of size 80 alloc'd
==4831==    at 0x4C2AB80: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==4831==    by 0x68EE88D: cv::fastMalloc(unsigned long) (alloc.cpp:64)
==4831==    by 0x69FE8A7: cv::String::allocate(unsigned long) (stl.cpp:50)
==4831==    by 0x4E4AB37: cv::String::operator=(char const*) (cvstd.hpp:668)
==4831==    by 0x5167A45: cv::BmpDecoder::BmpDecoder() (grfmt_bmp.cpp:55)
==4831==    by 0x513AD79: cv::Ptr<cv::BmpDecoder> cv::makePtr<cv::BmpDecoder>() (ptr.inl.hpp:301)
==4831==    by 0x5167CE3: cv::BmpDecoder::newDecoder() const (grfmt_bmp.cpp:76)
==4831==    by 0x51322DB: cv::findDecoder(cv::String const&) (loadsave.cpp:199)
==4831==    by 0x5134301: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:384)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831== 
==4831== Source and destination overlap in memcpy(0xecb67d4, 0xecb67f0, 47)
==4831==    at 0x4C2F71C: memcpy@@GLIBC_2.14 (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==4831==    by 0x5178F29: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:235)
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==4831==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831== 
nvalid read of size 1
==4831==    at 0x74ADAB0: __GI_mempcpy (memcpy.S:166)
==4831==    by 0x749A38D: _IO_file_xsgetn (fileops.c:1396)
==4831==    by 0x748F86E: fread (iofread.c:42)
==4831==    by 0x51784E2: cv::RBaseStream::readBlock() (bitstrm.cpp:105)
==4831==    by 0x5178F9E: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:233)
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==4831==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831==  Address 0x200040000ffffd1 is not stack'd, malloc'd or (recently) free'd
==4831== 
==4831== 
==4831== Process terminating with default action of signal 11 (SIGSEGV)
==4831==  General Protection Fault
==4831==    at 0x74ADAB0: __GI_mempcpy (memcpy.S:166)
==4831==    by 0x749A38D: _IO_file_xsgetn (fileops.c:1396)
==4831==    by 0x748F86E: fread (iofread.c:42)
==4831==    by 0x51784E2: cv::RBaseStream::readBlock() (bitstrm.cpp:105)
==4831==    by 0x5178F9E: cv::RLByteStream::getBytes(void*, int) (bitstrm.cpp:233)
==4831==    by 0x51683B8: cv::BmpDecoder::readHeader() (grfmt_bmp.cpp:122)
==4831==    by 0x5134548: cv::imread_(cv::String const&, int, int, cv::Mat*) (loadsave.cpp:412)
==4831==    by 0x5135741: cv::imread(cv::String const&, int) (loadsave.cpp:565)
==4831==    by 0x400D90: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/MedianBlur-test/opencv_test.elf)
==4831== 
==4831== HEAP SUMMARY:
==4831==     in use at exit: 97,526 bytes in 393 blocks
==4831==   total heap usage: 454 allocs, 61 frees, 107,534 bytes allocated
==4831== 
==4831== LEAK SUMMARY:
==4831==    definitely lost: 0 bytes in 0 blocks
==4831==    indirectly lost: 0 bytes in 0 blocks
==4831==      possibly lost: 8,163 bytes in 113 blocks
==4831==    still reachable: 89,363 bytes in 280 blocks
==4831==         suppressed: 0 bytes in 0 blocks
==4831== Rerun with --leak-check=full to see details of leaked memory
==4831== 
==4831== For counts of detected and suppressed errors, rerun with: -v
==4831== ERROR SUMMARY: 259 errors from 4 contexts (suppressed: 0 from 0)
Segmentation fault

```

# 9. Invalid write in icvCvt_BGRA2BGR_8u_C4C3R

```
==2971== Memcheck, a memory error detector
==2971== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==2971== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==2971== Command: ../../../../OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf id:000038,sig:06,src:000475,op:flip1,pos:21
==2971== 
==2971== Warning: set address range perms: large range [0x3a044040, 0x1ba074088) (undefined)
==2971== Invalid read of size 1
==2971==    at 0x506A270: icvCvt_BGRA2BGR_8u_C4C3R(unsigned char const*, int, unsigned char*, int, CvSize, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x507D7A8: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971==  Address 0xdf05b91 is 1 bytes after a block of size 16,416 alloc'd
==2971==    at 0x4C2B800: operator new[](unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==2971==    by 0x507DD8C: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971== 
==2971== Invalid read of size 1
==2971==    at 0x506A276: icvCvt_BGRA2BGR_8u_C4C3R(unsigned char const*, int, unsigned char*, int, CvSize, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x507D7A8: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971==  Address 0xdf05b90 is 0 bytes after a block of size 16,416 alloc'd
==2971==    at 0x4C2B800: operator new[](unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==2971==    by 0x507DD8C: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971== 
==2971== Invalid read of size 1
==2971==    at 0x506A290: icvCvt_BGRA2BGR_8u_C4C3R(unsigned char const*, int, unsigned char*, int, CvSize, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x507D7A8: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971==  Address 0xdf05b92 is 2 bytes after a block of size 16,416 alloc'd
==2971==    at 0x4C2B800: operator new[](unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==2971==    by 0x507DD8C: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971== 
==2971== 
==2971== Process terminating with default action of signal 11 (SIGSEGV)
==2971==  Access not within mapped region at address 0xE2E0001
==2971==    at 0x506A270: icvCvt_BGRA2BGR_8u_C4C3R(unsigned char const*, int, unsigned char*, int, CvSize, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x507D7A8: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5062D67: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x5063204: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build/install/lib/libopencv_imgcodecs.so.3.3.0)
==2971==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==2971==  If you believe this happened as a result of a stack
==2971==  overflow in your program's main thread (unlikely but
==2971==  possible), you can try to increase the size of the
==2971==  main thread stack using the --main-stacksize= flag.
==2971==  The main thread stack size used in this run was 8388608.
==2971== 
==2971== HEAP SUMMARY:
==2971==     in use at exit: 6,442,761,614 bytes in 397 blocks
==2971==   total heap usage: 458 allocs, 61 frees, 6,442,771,622 bytes allocated
==2971== 
==2971== LEAK SUMMARY:
==2971==    definitely lost: 0 bytes in 0 blocks
==2971==    indirectly lost: 0 bytes in 0 blocks
==2971==      possibly lost: 6,442,655,739 bytes in 114 blocks
==2971==    still reachable: 105,875 bytes in 283 blocks
==2971==         suppressed: 0 bytes in 0 blocks
==2971== Rerun with --leak-check=full to see details of leaked memory
==2971== 
==2971== For counts of detected and suppressed errors, rerun with: -v
==2971== ERROR SUMMARY: 3029845 errors from 3 contexts (suppressed: 0 from 0)
Segmentation fault

```
![](./pics/bug8.PNG)


# 10. DOS (CPU exhaust )

the bug results cpu exhaust for a long time.

# 11. DOS (memory exhaust)

This bug results to memory exhaust. 

![](./pics/dos.PNG)


# 12. out-of-bound write in FillColorRow1

```
==16048== Memcheck, a memory error detector
==16048== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==16048== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==16048== Command: ./opencv_test.elf ./12-opencv-outbound-write-FillColorRow1
==16048==
==16048== Warning: set address range perms: large range [0x3a044080, 0xccce9780) (undefined)
==16048== Invalid write of size 4
==16048==    at 0x50AD680: FillColorRow1(unsigned char*, unsigned char*, int, PaletteEntry*) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50BCB10: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50A384C: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50A3DB4: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==16048==  Address 0xffffffffccce04c8 is not stack'd, malloc'd or (recently) free'd
==16048==
==16048==
==16048== Process terminating with default action of signal 11 (SIGSEGV)
==16048==  Access not within mapped region at address 0xFFFFFFFFCCCE04C8
==16048==    at 0x50AD680: FillColorRow1(unsigned char*, unsigned char*, int, PaletteEntry*) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50BCB10: cv::BmpDecoder::readData(cv::Mat&) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50A384C: cv::imread_(cv::String const&, int, int, cv::Mat*) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x50A3DB4: cv::imread(cv::String const&, int) (in /data/xqx/tests/opencv-test/build-20170822/install/lib/libopencv_imgcodecs.so.3.3.0)
==16048==    by 0x400DFA: main (in /data/xqx/tests/opencv-test/OpenCV3-Intro-Book-Src/Linux-OpenCV3-examples/GaussianBlur-test/opencv_test.elf)
==16048==  If you believe this happened as a result of a stack
==16048==  overflow in your program's main thread (unlikely but
==16048==  possible), you can try to increase the size of the
==16048==  main thread stack using the --main-stacksize= flag.
==16048==  The main thread stack size used in this run was 8388608.
==16048==
==16048== HEAP SUMMARY:
==16048==     in use at exit: 2,462,831,174 bytes in 397 blocks
==16048==   total heap usage: 458 allocs, 61 frees, 2,462,840,750 bytes allocated
==16048==
==16048== LEAK SUMMARY:
==16048==    definitely lost: 0 bytes in 0 blocks
==16048==    indirectly lost: 0 bytes in 0 blocks
==16048==      possibly lost: 5,324 bytes in 105 blocks
==16048==    still reachable: 2,462,825,850 bytes in 292 blocks
==16048==         suppressed: 0 bytes in 0 blocks
==16048== Rerun with --leak-check=full to see details of leaked memory
==16048==
==16048== For counts of detected and suppressed errors, rerun with: -v
==16048== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
Segmentation fault


```

# 13. DOS, exhaust CPU for 10 hours.

a new DOS testcase in opencv after a patch in 20170823,
it could exhaust cpu for more than 10 hours.



![](./pics/dos-10h.PNG)
