- [Description](#description)
- [version](#version)
- [others](#others)
    - [@_@](#)
- [Detial](#detial)
- [vuln/RIFF-Chunk-Read_Out-Of-Bounds-Read](#vuln-riff-chunk-read-out-of-bounds-read)
    - [target](#target)
    - [asan report](#asan-report)
- [vuln/RIFF-Chunk-Read_heap-buffer-overflow](#vuln-riff-chunk-read-heap-buffer-overflow)
    - [target](#target)
    - [asan report](#asan-report)
- [vuln/DLS-Info-UpdateChunks_out-of-bounds-write](#vuln-dls-info-updatechunks-out-of-bounds-write)
    - [targets](#targets)
    - [gdb info](#gdb-info)
- [vuln/gig-Region-UpdateChunks:3310-35_out-of-bounds-read](#vuln-gig-region-updatechunks-3310-35-out-of-bounds-read)
    - [target](#target)
    - [gdb info](#gdb-info)
    - [asan report](#asan-report)
- [vuln/gig-Region-UpdateChunks:3303_out-of-bounds-read.gig](#vuln-gig-region-updatechunks-3303-out-of-bounds-readgig)
    - [target](#target)
    - [gdb info](#gdb-info)
- [vuln/DLS-Info-SaveString_out-of-bounds-write.gig](#vuln-dls-info-savestring-out-of-bounds-writegig)
    - [target](#target)
    - [gdb backtrace](#gdb-backtrace)
    - [asan report](#asan-report)
- [vuln/store16_heap-buffer-overflow.gig](#vuln-store16-heap-buffer-overflowgig)
    - [target](#target)
    - [asan report](#asan-report)
- [vuln/gig-File-UpdateChunks_out-of-bounds-read.gig](#vuln-gig-file-updatechunks-out-of-bounds-readgig)
    - [target](#target)
    - [gdb info](#gdb-info)
- [vuln/store32_heap-buffer-overflow.gig](#vuln-store32-heap-buffer-overflowgig)
    - [target](#target)
    - [asan report](#asan-report)
- [vuln/store32_out-of-bounds-write.gig](#vuln-store32-out-of-bounds-writegig)
    - [target](#target)
    - [gdb info](#gdb-info)
    - [asan report](#asan-report)
- [vuln/store16_out-of-bounds-write.gig](#vuln-store16-out-of-bounds-writegig)
    - [target](#target)
    - [gdb info](#gdb-info)
    - [asan report](#asan-report)
    - [gdb info](#gdb-info)

# Description
libgig is a C++ library for loading, modifying existing and creating new Gigasampler (.gig) files and DLS (Downloadable Sounds) Level 1/2 files, KORG sample based instruments (.KSF and .KMP files), SoundFont v2 (.sf2) files and AKAI sampler data. The source code package includes a couple of command line tools based on the library. The library and tools are released in source code format under the GNU General Public License, except the AKAI classes which are released under the GNU Lesser General Public License.
link：http://www.linuxsampler.org/libgig/
# version
libgig 4.1.0

# others
## @_@
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detial


# vuln/RIFF-Chunk-Read_Out-Of-Bounds-Read
## target
./gigextract vuln/RIFF-Chunk-Read_Out-Of-Bounds-Read /tmp/gigTrash/
## asan report
```
 ► 323         if (ullPos >= ullCurrentChunkSize) return 0;

Seeking for available samples...OK
Extracting Sample 1) (NO NAME) (16Bits, 44100Hz, 1 Channels, 0 Samples)...AddressSanitizer:DEADLYSIGNAL
=================================================================
==14182==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000038 (pc 0x7fb886711c08 bp 0x000000761e40 sp 0x7fff8b44a1c0 T0)
==14182==The signal is caused by a READ memory access.
==14182==Hint: address points to the zero page.
    #0 0x7fb886711c07 in RIFF::Chunk::Read(void*, unsigned long, unsigned long) /home/fuzzing/libgig-4.1.0/src/RIFF.cpp:323:23
    #1 0x7fb88679c10e in gig::Sample::Read(void*, unsigned long, gig::buffer_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:1143:49
    #2 0x523807 in ExtractSamples(gig::File*, char*, std::map<unsigned int, bool, std::less<unsigned int>, std::allocator<std::pair<unsigned int const, bool> > >*) /home/fuzzing/libgig-4.1.0/src/tools/gigextract.cpp:263:38
    #3 0x51d63c in main /home/fuzzing/libgig-4.1.0/src/tools/gigextract.cpp:162:9
    #4 0x7fb8851ea82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #5 0x41baf8 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gigextract+0x41baf8)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fuzzing/libgig-4.1.0/src/RIFF.cpp:323:23 in RIFF::Chunk::Read(void*, unsigned long, unsigned long)
==14182==ABORTING

```

# vuln/RIFF-Chunk-Read_heap-buffer-overflow
## target
```
./gigextract vuln/RIFF-Chunk-Read_heap-buffer-overflow /tmp/gigTrash/
```
## asan report
```
Seeking for available samples...OK
Extracting Sample 1) "GH1         " (16Bits, 44100Hz, 9 Channels, 2055 Samples, LoopType normal, LoopStart 17499, LoopEnd 18496)...=================================================================
==64374==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x62d00000947e at pc 0x00000048f4ef bp 0x7ffc47b7cab0 sp 0x7ffc47b7c260
WRITE of size 4004 at 0x62d00000947e thread T0
    #0 0x48f4ee in read /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/../sanitizer_common/sanitizer_common_interceptors.inc:960
    #1 0x7faa853a5d8c in RIFF::Chunk::Read(void*, unsigned long, unsigned long) /home/fuzzing/libgig-4.1.0/src/RIFF.cpp:327:29
    #2 0x7faa8543010e in gig::Sample::Read(void*, unsigned long, gig::buffer_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:1143:49
    #3 0x523807 in ExtractSamples(gig::File*, char*, std::map<unsigned int, bool, std::less<unsigned int>, std::allocator<std::pair<unsigned int const, bool> > >*) /home/fuzzing/libgig-4.1.0/src/tools/gige
xtract.cpp:263:38
    #4 0x51d63c in main /home/fuzzing/libgig-4.1.0/src/tools/gigextract.cpp:162:9
    #5 0x7faa83e7e82f in     __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #6 0x41baf8 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gigextract+0x41baf8)

0x62d00000947e is located 0 bytes to the right of 36990-byte region [0x62d000000400,0x62d00000947e)
allocated by thread T0 here:
    #0 0x517968 in operator new[](unsigned long) /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:95
    #1 0x523786 in ExtractSamples(gig::File*, char*, std::map<unsigned int, bool, std::less<unsigned int>, std::allocator<std::pair<unsigned int const, bool> > >*) /home/fuzzing/libgig-4.1.0/src/tools/gige
xtract.cpp:254:21
    #2 0x51d63c in main /home/fuzzing/libgig-4.1.0/src/tools/gigextract.cpp:162:9
    #3 0x7faa83e7e82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/../sanitizer_common/sanitizer_common_interceptors.inc:960 in read
Shadow bytes around the buggy address:
  0x0c5a7fff9230: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff9240: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff9250: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff9260: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff9270: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c5a7fff9280: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00[06]
  0x0c5a7fff9290: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff92a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff92b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff92c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff92d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==64374==ABORTING

```


# vuln/DLS-Info-UpdateChunks_out-of-bounds-write

## targets
```
./gigmerge vuln/DLS-Info-UpdateChunks_out-of-bounds-write-1.gig  vuln/DLS-Info-UpdateChunks_out-of-bounds-write-2.gig out.gig
```
## gdb info

```
Program received signal SIGSEGV, Segmentation fault.
__strncpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S:315
315	../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S: No such file or directory.
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────────────────────────────────────[ REGISTERS ]──────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x7fffffffd2a0 —▸ 0x7fffffffd2b0 ◂— 0x3420676967626900
 RCX  0x0
 RDX  0x0
 RDI  0x0
*RSI  0x555555774dc0 ◂— 0x2020202020202020 ('        ')
*R8   0x100
 R9   0x0
*R10  0x7
*R11  0x7ffff7257b70 (__strncpy_sse2_unaligned) ◂— mov    r8, rdx
*R12  0x55555577e0a0 —▸ 0x7ffff7dd1fc0 —▸ 0x7ffff7b64920 (RIFF::List::~List()) ◂— mov    rax, qword ptr [rip + 0x26e681]
*R13  0x7fffffffd1a0 —▸ 0x7fffffffd1b0 ◂— 0x454d414e4f4e /* 'NONAME' */
*R14  0x7fffffffd1e0 —▸ 0x7fffffffd1f0 ◂— 'libgig 4.1.0'
*R15  0x7fffffffd200 —▸ 0x555555773490 ◂— 0x2064657461657243 ('Created ')
*RBP  0x555555774ad0 —▸ 0x7ffff7dd2200 —▸ 0x7ffff7b68a30 (DLS::Info::~Info()) ◂— mov    rax, qword ptr [rip + 0x26a429]
*RSP  0x7fffffffd158 —▸ 0x7ffff7b6e79a (DLS::Info::UpdateChunks(RIFF::progress_t*)+282) ◂— mov    rdi, qword ptr [rsp + 0x140]
*RIP  0x7ffff7257e39 (__strncpy_sse2_unaligned+713) ◂— movdqu xmmword ptr [rdi], xmm1
───────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────
 ► 0x7ffff7257e39 <__strncpy_sse2_unaligned+713>     movdqu xmmword ptr [rdi], xmm1
   0x7ffff7257e3d <__strncpy_sse2_unaligned+717>     pmovmskb edx, xmm0
   0x7ffff7257e41 <__strncpy_sse2_unaligned+721>     cmp    r8, 0x21
   0x7ffff7257e45 <__strncpy_sse2_unaligned+725>     jbe    __strncpy_sse2_unaligned+1344 <0x7ffff72580b0>
    ↓
   0x7ffff72580b0 <__strncpy_sse2_unaligned+1344>    add    rdi, 0x10
   0x7ffff72580b4 <__strncpy_sse2_unaligned+1348>    add    rsi, 0x10
   0x7ffff72580b8 <__strncpy_sse2_unaligned+1352>    sub    r8, 0x10
   0x7ffff72580bc <__strncpy_sse2_unaligned+1356>    test   rdx, rdx
   0x7ffff72580bf <__strncpy_sse2_unaligned+1359>    jne    __strncpy_sse2_unaligned+1201 <0x7ffff7258021>
    ↓
   0x7ffff7258021 <__strncpy_sse2_unaligned+1201>    bsf    rdx, rdx
   0x7ffff7258025 <__strncpy_sse2_unaligned+1205>    cmp    rdx, r8
───────────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd158 —▸ 0x7ffff7b6e79a (DLS::Info::UpdateChunks(RIFF::progress_t*)+282) ◂— mov    rdi, qword ptr [rsp + 0x140]
01:0008│      0x7fffffffd160 ◂— 0x4000000000000000
02:0010│      0x7fffffffd168 —▸ 0x7fffffffd1c0 —▸ 0x7fffffffd1d0 ◂— '2018-07-13'
03:0018│      0x7fffffffd170 —▸ 0x7fffffffd280 —▸ 0x7fffffffd290 ◂— 0x302e312e34 /* '4.1.0' */
04:0020│      0x7fffffffd178 —▸ 0x7fffffffd260 —▸ 0x7fffffffd270 ◂— 0x3420676967626900
05:0028│      0x7fffffffd180 —▸ 0x7fffffffd240 —▸ 0x7fffffffd250 ◂— 0x20676967626900
06:0030│      0x7fffffffd188 ◂— 0x0
07:0038│      0x7fffffffd190 —▸ 0x7fffffffd3a0 ◂— 0x0
─────────────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────────────
 ► f 0     7ffff7257e39 __strncpy_sse2_unaligned+713
   f 1     7ffff7b6e79a DLS::Info::UpdateChunks(RIFF::progress_t*)+282
   f 2     7ffff7b692ae DLS::Resource::UpdateChunks(RIFF::progress_t*)+14
   f 3     7ffff7b69609 DLS::File::UpdateChunks(RIFF::progress_t*)+41
   f 4     7ffff7b96bbe gig::File::UpdateChunks(RIFF::progress_t*)+206
   f 5     7ffff7b6de4c
   f 6     7ffff7b9386f gig::File::AddContentOf(gig::File*)+5423
   f 7     5555555556fc main+620
   f 8     7ffff71c2b97 __libc_start_main+231
Program received signal SIGSEGV (fault address 0x0)
pwndbg> bt
#0  __strncpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S:315
#1  0x00007ffff7b6e79a in DLS::Info::UpdateChunks (this=0x555555774ad0, pProgress=<optimized out>) at DLS.cpp:383
#2  0x00007ffff7b692ae in DLS::Resource::UpdateChunks (this=0x555555774950, pProgress=<optimized out>) at DLS.cpp:477
#3  0x00007ffff7b69609 in DLS::File::UpdateChunks (this=this@entry=0x555555774950, pProgress=pProgress@entry=0x7fffffffd520) at DLS.cpp:1700
#4  0x00007ffff7b96bbe in gig::File::UpdateChunks (this=0x555555774950, pProgress=0x7fffffffd520) at gig.cpp:6345
#5  0x00007ffff7b6de4c in DLS::File::Save (this=this@entry=0x555555774950, Path="1", pProgress=pProgress@entry=0x0) at DLS.cpp:1809
#6  0x00007ffff7b9386f in gig::File::AddContentOf (this=0x555555774950, pFile=0x5555557728a0) at gig.cpp:5866
#7  0x00005555555556fc in main (argc=argc@entry=4, argv=argv@entry=0x7fffffffdbe8) at gigmerge.cpp:116
#8  0x00007ffff71c2b97 in __libc_start_main (main=0x555555555490 <main(int, char**)>, argc=4, argv=0x7fffffffdbe8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdbd8) at ../csu/libc-start.c:310
#9  0x0000555555555d7a in _start ()
```

# vuln/gig-Region-UpdateChunks:3310-35_out-of-bounds-read
## target
```
gig2stereo @@
```
## gdb info
```
backtrace:
#0  0x00007ffff7b9603b in gig::Region::UpdateChunks (this=0x55555577fda0, pProgress=0x7fffffffcea0) at gig.cpp:3310
#1  0x00007ffff7b6950b in DLS::Instrument::UpdateChunks (this=this@entry=0x55555577e940, pProgress=pProgress@entry=0x7fffffffcf80) at DLS.cpp:1336
#2  0x00007ffff7b96655 in gig::Instrument::UpdateChunks (this=0x55555577e940, pProgress=0x7fffffffcf80) at gig.cpp:4801
#3  0x00007ffff7b69af1 in DLS::File::UpdateChunks (this=this@entry=0x7fffffffd4f0, pProgress=pProgress@entry=0x7fffffffd130) at DLS.cpp:1734
#4  0x00007ffff7b96bbe in gig::File::UpdateChunks (this=0x7fffffffd4f0, pProgress=0x7fffffffd130) at gig.cpp:6345
#5  0x00007ffff7b6dfc4 in DLS::File::Save (this=0x7fffffffd4f0, pProgress=0x0) at DLS.cpp:1839
#6  0x000055555555a6df in convertFileToStereo (path=..., keep=<optimized out>, forceReplace=false, skipIncompatible=true, verbose=0) at gig2stereo.cpp:388
#7  0x000055555555712c in main (argc=argc@entry=2, argv=argv@entry=0x7fffffffd888) at gig2stereo.cpp:664
#8  0x00007ffff71c2b97 in __libc_start_main (main=0x555555556a10 <main(int, char**)>, argc=2, argv=0x7fffffffd888, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffd878) at ../csu/libc-start.c:310
#9  0x000055555555794a in _start ()
src info:
3305	        // first update base class's chunks
3306	        DLS::Region::UpdateChunks(pProgress);
3307	
3308	        // update dimension region's chunks
3309	        for (int i = 0; i < DimensionRegions; i++) {
3310	            pDimensionRegions[i]->UpdateChunks(pProgress);
3311	        }
3312	
3313	        File* pFile = (File*) GetParent()->GetParent();
3314	        bool version3 = pFile->pVersion && pFile->pVersion->major == 3;
register info:
rax            0x0	0
rbx            0x55555577fda0	93824994508192
rcx            0x5	5
rdx            0x1	1
rsi            0x7fffffffcea0	140737488342688
rdi            0x0	0
rbp            0x2	0x2
rsp            0x7fffffffce20	0x7fffffffce20
r8             0x0	0
r9             0x0	0
r10            0x1	1
r11            0x1	1
r12            0x7fffffffcea0	140737488342688
r13            0x55555577fa40	93824994507328
r14            0x1	1
r15            0x7fffffffcea0	140737488342688
rip            0x7ffff7b9603b	0x7ffff7b9603b <gig::Region::UpdateChunks(RIFF::progress_t*)+91>
eflags         0x10202	[ IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0

```
## asan report
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==5624==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f0c6cc5ebea bp 0x7ffd45281310 sp 0x7ffd452811c0 T0)
==5624==The signal is caused by a READ memory access.
==5624==Hint: address points to the zero page.
    #0 0x7f0c6cc5ebe9 in gig::Region::UpdateChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/gig.cpp:3310:35
    #1 0x7f0c6cbf52bc in DLS::Instrument::UpdateChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1336:22
    #2 0x7f0c6cc86e6d in gig::Instrument::UpdateChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/gig.cpp:4801:26
    #3 0x7f0c6cbfc37b in DLS::File::UpdateChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1734:26
    #4 0x7f0c6cca64b6 in gig::File::UpdateChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/gig.cpp:6345:20
    #5 0x7f0c6cbfe201 in DLS::File::Save(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1839:13
    #6 0x526793 in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #7 0x51c522 in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #8 0x7f0c6b825b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #9 0x41c3a9 in _start (/home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed-asan/bin/gig2stereo+0x41c3a9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/gig.cpp:3310:35 in gig::Region::UpdateChunks(RIFF::progress_t*)
==5624==ABORTING

```
# vuln/gig-Region-UpdateChunks:3303_out-of-bounds-read.gig
## target
```
./gig2stereo vuln/gig-Region-UpdateChunks_out-of-bounds-read.gig 
```

## gdb info
```
Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7b9600b in gig::Region::UpdateChunks (this=0x555555789d80, pProgress=0x7fffffffd230) at gig.cpp:3303
3303	        pSample = pDimensionRegions[0]->pSample;
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x555555789d80 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RCX  0xffffffff
*RDX  0x20
*RDI  0x555555789d80 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RSI  0x7fffffffd230 ◂— 0x0
*R8   0xffffffff
*R9   0xffffffff
*R10  0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*R11  0x555555783c60 —▸ 0x7ffff7dd26c0 —▸ 0x7ffff7b95210 (gig::Sample::UpdateChunks(RIFF::progress_t*)) ◂— push   r12
*R12  0x7fffffffd230 ◂— 0x0
*R13  0x55555577ef30 —▸ 0x555555787260 —▸ 0x555555788730 —▸ 0x555555789d60 —▸ 0x55555578ae60 ◂— ...
*R14  0x4
*R15  0x7fffffffd230 ◂— 0x0
*RBP  0x55555577dd30 —▸ 0x7ffff7dd28a0 —▸ 0x7ffff7b96640 (gig::Instrument::UpdateChunks(RIFF::progress_t*)) ◂— push   r13
*RSP  0x7fffffffd1b0 —▸ 0x7fffffffd310 ◂— 0x0
*RIP  0x7ffff7b9600b (gig::Region::UpdateChunks(RIFF::progress_t*)+43) ◂— mov    rdx, qword ptr [rax + 0x38]
─────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────
 ► 0x7ffff7b9600b <gig::Region::UpdateChunks(RIFF::progress_t*)+43>    mov    rdx, qword ptr [rax + 0x38]
   0x7ffff7b9600f <gig::Region::UpdateChunks(RIFF::progress_t*)+47>    mov    qword ptr [rdi + 0xa0], rdx
   0x7ffff7b96016 <gig::Region::UpdateChunks(RIFF::progress_t*)+54>    call   DLS::Region::UpdateChunks(RIFF::progress_t*)@plt <0x7ffff7b54550>
 
   0x7ffff7b9601b <gig::Region::UpdateChunks(RIFF::progress_t*)+59>    mov    r9d, dword ptr [rbx + 0x130]
   0x7ffff7b96022 <gig::Region::UpdateChunks(RIFF::progress_t*)+66>    test   r9d, r9d
   0x7ffff7b96025 <gig::Region::UpdateChunks(RIFF::progress_t*)+69>    je     gig::Region::UpdateChunks(RIFF::progress_t*)+111 <0x7ffff7b9604f>
 
   0x7ffff7b96027 <gig::Region::UpdateChunks(RIFF::progress_t*)+71>    mov    ebp, 1
   0x7ffff7b9602c <gig::Region::UpdateChunks(RIFF::progress_t*)+76>    nop    dword ptr [rax]
   0x7ffff7b96030 <gig::Region::UpdateChunks(RIFF::progress_t*)+80>    mov    rdi, qword ptr [rbx + rbp*8 + 0x130]
   0x7ffff7b96038 <gig::Region::UpdateChunks(RIFF::progress_t*)+88>    mov    rsi, r12
   0x7ffff7b9603b <gig::Region::UpdateChunks(RIFF::progress_t*)+91>    mov    rcx, qword ptr [rdi]
──────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]──────────────────────────────────────────────────────────────────────
   3298     void Region::UpdateChunks(progress_t* pProgress) {
   3299         // in the gig format we don't care about the Region's sample reference
   3300         // but we still have to provide some existing one to not corrupt the
   3301         // file, so to avoid the latter we simply always assign the sample of
   3302         // the first dimension region of this region
 ► 3303         pSample = pDimensionRegions[0]->pSample;
   3304 
   3305         // first update base class's chunks
   3306         DLS::Region::UpdateChunks(pProgress);
   3307 
   3308         // update dimension region's chunks
──────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd1b0 —▸ 0x7fffffffd310 ◂— 0x0
01:0008│      0x7fffffffd1b8 —▸ 0x55555577dbd0 —▸ 0x55555578dae0 ◂— 0x55555577dbd0
02:0010│      0x7fffffffd1c0 —▸ 0x55555578dae0 —▸ 0x55555577dbd0 ◂— 0x55555578dae0
03:0018│      0x7fffffffd1c8 —▸ 0x7ffff72380fc (malloc+140) ◂— test   rax, rax
04:0020│      0x7fffffffd1d0 ◂— 0x0
05:0028│      0x7fffffffd1d8 —▸ 0x7ffff78d5020 ◂— cmp    rax, rbx
06:0030│      0x7fffffffd1e0 ◂— 0x0
07:0038│      0x7fffffffd1e8 ◂— 0x2c7ef34cba469200
────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7b9600b gig::Region::UpdateChunks(RIFF::progress_t*)+43
   f 1     7ffff7b6950b DLS::Instrument::UpdateChunks(RIFF::progress_t*)+459
   f 2     7ffff7b96655 gig::Instrument::UpdateChunks(RIFF::progress_t*)+21
   f 3     7ffff7b69af1 DLS::File::UpdateChunks(RIFF::progress_t*)+1297
   f 4     7ffff7b96bbe gig::File::UpdateChunks(RIFF::progress_t*)+206
   f 5     7ffff7b6dfc4 DLS::File::Save(RIFF::progress_t*)+340
   f 6     55555555a6df
   f 7     55555555712c main+1820
   f 8     7ffff71c2b97 __libc_start_main+231
Program received signal SIGSEGV (fault address 0x38)
```


# vuln/DLS-Info-SaveString_out-of-bounds-write.gig
## target
```
./gig2stereo vuln/DLS-Info-SaveString_out-of-bounds-write.gig
```
## gdb backtrace
```
#0  __strncpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/strcpy-sse2-unaligned.S:534
#1  0x0000000000447abc in __interceptor_strncpy (to=0x0, from=0x616000000098 "", size=128) at /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors.cc:440
#2  0x00007ffff7a0f643 in SaveString (ChunkID=<optimized out>, ck=<optimized out>, lstINFO=<optimized out>, s=..., sDefault=..., bUseFixedLengthStrings=true, size=<optimized out>) at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/bits/basic_string.h:135
#3  0x00007ffff79f1172 in DLS::Info::SaveString (this=0x616000000080, ChunkID=1296125513, s=Python Exception <class 'gdb.error'> There is no member named _M_dataplus.: 
, sDefault=..., lstINFO=<optimized out>) at DLS.cpp:336
#4  DLS::Info::UpdateChunks (this=0x616000000080, pProgress=<optimized out>) at DLS.cpp:393
#5  0x00007ffff79f4b0f in DLS::Resource::UpdateChunks (this=0x7fffffffcbc0, pProgress=0x7fffffffc840) at DLS.cpp:477
#6  0x00007ffff7a098fb in DLS::File::UpdateChunks (this=0x7fffffffcbc0, pProgress=0x7fffffffc840) at DLS.cpp:1700
#7  0x00007ffff7ab2638 in gig::File::UpdateChunks (this=<optimized out>, pProgress=0x7fffffffc840) at gig.cpp:6345
#8  0x00007ffff7a0c1bf in DLS::File::Save (this=0x7fffffffcbc0, pProgress=<optimized out>) at DLS.cpp:1839
#9  0x0000000000529d7d in convertFileToStereo (path=..., keep=false, forceReplace=false, skipIncompatible=true, verbose=0) at gig2stereo.cpp:388
#10 0x000000000051fea9 in main (argc=17008, argc@entry=2, argv=0xffffffffa9f, argv@entry=0x7fffffffdbc8) at gig2stereo.cpp:661
#11 0x00007ffff6635b97 in __libc_start_main (main=0x51c430 <main(int, char**)>, argc=2, argv=0x7fffffffdbc8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdbb8) at ../csu/libc-start.c:310
#12 0x000000000041c429 in _start ()

```
## asan report 
```
=================================================================
==102173==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f078be82570 bp 0x7ffdf3eb85d0 sp 0x7ffdf3eb7d48 T0)
==102173==The signal is caused by a WRITE memory access.
==102173==Hint: address points to the zero page.
    #0 0x7f078be8256f  (/lib/x86_64-linux-gnu/libc.so.6+0xa656f)
    #1 0x447abb in strncpy /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors.cc:440
    #2 0x7f078d10b642 in SaveString(unsigned int, RIFF::Chunk*, RIFF::List*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, int) /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/bits/basic_string.h
    #3 0x7f078d0ed171 in DLS::Info::SaveString(unsigned int, RIFF::List*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:336:9
    #4 0x7f078d0ed171 in DLS::Info::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:393
    #5 0x7f078d0f0b0e in DLS::Resource::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:477:16
    #6 0x7f078d1058fa in DLS::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1700:19
    #7 0x7f078d1ae637 in gig::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:6345:20
    #8 0x7f078d1081be in DLS::File::Save(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1839:13
    #9 0x529d7c in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #10 0x51fea8 in main /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #11 0x7f078bdfc82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #12 0x41c428 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gig2stereo+0x41c428)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0xa656f) 
==102173==ABORTING

```

# vuln/store16_heap-buffer-overflow.gig

## target
```
./gig2stereo vuln/store16_heap-buffer-overflow.gig
```

## asan report
```
==112978==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000131 at pc 0x7f301a5082e0 bp 0x7fffa57fb690 sp 0x7fffa57fb688
WRITE of size 1 at 0x602000000131 thread T0
    #0 0x7f301a5082df in store16(unsigned char*, uns igned short) /home/fuzzing/libgig-4.1.0/src/./helper.h:115:14
    #1 0x7f301a5082df in DLS::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1707
    #2 0x7f301a5af637 in gig::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:6345:20
    #3 0x7f301a5091be in DLS::File::Save(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1839:13
    #4 0x529d7c in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #5 0x51fea8 in main /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #6 0x7f30191fd82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #7 0x41c428 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gig2stereo+0x41c428)

0x602000000131 is located 0 bytes to the right of 1-byte region [0x602000000130,0x602000000131)
allocated by thread T0 here:
    #0 0x518298 in operator new[](unsigned long) /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:95
    #1 0x7f301a4c18e0 in RIFF::Chunk::LoadChunkData() /home/fuzzing/libgig-4.1.0/src/RIFF.cpp:821:26

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fuzzing/libgig-4.1.0/src/./helper.h:115:14 in store16(unsigned char*, unsigned short)
Shadow bytes around the buggy address:
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff8000: fa fa fd fd fa fa fd fd fa fa 00 00 fa fa 00 fa
  0x0c047fff8010: fa fa fd fd fa fa fd fd fa fa 00 00 fa fa 00 00
=>0x0c047fff8020: fa fa 00 00 fa fa[01]fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==112978==ABORTING

```


# vuln/gig-File-UpdateChunks_out-of-bounds-read.gig

## target 
```
 ./gig2stereo vuln/gig-File-UpdateChunks_out-of-bounds-read
```

## gdb info
```

Starting program: /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed/bin/gig2stereo crashes-ste/04.gig
Converting file 1/1: crashes-ste/04.gig ... 
Program received signal SIGSEGV, Segmentation fault.
gig::File::UpdateChunks (this=0x7fffffffd890, pProgress=0x7fffffffd4d0) at gig.cpp:6402
6402	        int sublen = int(pSamples->size() / 8 + 49);
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]─────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x7fffffffd890 —▸ 0x7ffff7dd2940 —▸ 0x7ffff7b96af0 (gig::File::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RCX  0x7fffffffd890 —▸ 0x7ffff7dd2940 —▸ 0x7ffff7b96af0 (gig::File::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
 RDX  0x0
*RDI  0x7fffffffd7d0 —▸ 0x7ffff7dd1ff8 —▸ 0x7ffff7b64990 (RIFF::File::~File()) ◂— mov    rax, qword ptr [rip + 0x26e599]
 RSI  0x0
*R8   0x7fffffffd7d0 —▸ 0x7ffff7dd1ff8 —▸ 0x7ffff7b64990 (RIFF::File::~File()) ◂— mov    rax, qword ptr [rip + 0x26e599]
 R9   0x0
*R10  0x8
*R11  0x1
*R12  0x7fffffffd4d0 ◂— 0x0
*R13  0x7fffffffd890 —▸ 0x7ffff7dd2940 —▸ 0x7ffff7b96af0 (gig::File::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*R14  0x7fffffffd6c8 ◂— 0xffffffff00000000
*R15  0x7fffffffd698 ◂— 0xffffffff00000000
*RBP  0x555555c66270 —▸ 0x7ffff7dd1fc0 —▸ 0x7ffff7b64920 (RIFF::List::~List()) ◂— mov    rax, qword ptr [rip + 0x26e681]
*RSP  0x7fffffffd390 ◂— 0x0
*RIP  0x7ffff7b96c6b (gig::File::UpdateChunks(RIFF::progress_t*)+379) ◂— mov    r8, qword ptr [rsi + 0x10]
──────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x7ffff7b96c6b <gig::File::UpdateChunks(RIFF::progress_t*)+379>    mov    r8, qword ptr [rsi + 0x10]
   0x7ffff7b96c6f <gig::File::UpdateChunks(RIFF::progress_t*)+383>    lea    r12d, [r9 + 1]
   0x7ffff7b96c73 <gig::File::UpdateChunks(RIFF::progress_t*)+387>    mov    esi, 0x666e6965
   0x7ffff7b96c78 <gig::File::UpdateChunks(RIFF::progress_t*)+392>    mov    dword ptr [rsp + 8], r9d
   0x7ffff7b96c7d <gig::File::UpdateChunks(RIFF::progress_t*)+397>    shr    r8, 3
   0x7ffff7b96c81 <gig::File::UpdateChunks(RIFF::progress_t*)+401>    add    r8d, 0x31
   0x7ffff7b96c85 <gig::File::UpdateChunks(RIFF::progress_t*)+405>    imul   r12d, r8d
   0x7ffff7b96c89 <gig::File::UpdateChunks(RIFF::progress_t*)+409>    mov    dword ptr [rsp + 0x5c], r8d
   0x7ffff7b96c8e <gig::File::UpdateChunks(RIFF::progress_t*)+414>    call   0x7ffff7b55a10
 
   0x7ffff7b96c93 <gig::File::UpdateChunks(RIFF::progress_t*)+419>    test   rax, rax
   0x7ffff7b96c96 <gig::File::UpdateChunks(RIFF::progress_t*)+422>    mov    qword ptr [rsp + 0x78], rax
───────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────────────────────────────────────────
   6397         // by the file/instrument.
   6398         //
   6399         // Note that there are several fields with unknown use. These
   6400         // are set to zero.
   6401 
 ► 6402         int sublen = int(pSamples->size() / 8 + 49);
   6403         int einfSize = (Instruments + 1) * sublen;
   6404 
   6405         RIFF::Chunk* einf = pRIFF->GetSubChunk(CHUNK_ID_EINF);
   6406         if (einf) {
   6407             if (einf->GetSize() != einfSize) {
───────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd390 ◂— 0x0
... ↓
03:0018│      0x7fffffffd3a8 —▸ 0x55555577ceb0 —▸ 0x7ffff7dd1fc0 —▸ 0x7ffff7b64920 (RIFF::List::~List()) ◂— mov    rax, qword ptr [rip + 0x26e681]
04:0020│      0x7fffffffd3b0 ◂— 0x0
... ↓
─────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7b96c6b gig::File::UpdateChunks(RIFF::progress_t*)+379
   f 1     7ffff7b6dfc4 DLS::File::Save(RIFF::progress_t*)+340
   f 2     55555555a6df
   f 3     55555555712c main+1820
   f 4     7ffff71c2b97 __libc_start_main+231
Program received signal SIGSEGV (fault address 0x10)
pwndbg> by
Undefined command: "by".  Try "help".
pwndbg> bt
#0  gig::File::UpdateChunks (this=0x7fffffffd890, pProgress=0x7fffffffd4d0) at gig.cpp:6402
#1  0x00007ffff7b6dfc4 in DLS::File::Save (this=0x7fffffffd890, pProgress=0x0) at DLS.cpp:1839
#2  0x000055555555a6df in convertFileToStereo (path=..., keep=<optimized out>, forceReplace=false, skipIncompatible=true, verbose=0) at gig2stereo.cpp:388
#3  0x000055555555712c in main (argc=argc@entry=2, argv=argv@entry=0x7fffffffdc28) at gig2stereo.cpp:664
#4  0x00007ffff71c2b97 in __libc_start_main (main=0x555555556a10 <main(int, char**)>, argc=2, argv=0x7fffffffdc28, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdc18) at ../csu/libc-start.c:310
#5  0x000055555555794a in _start ()

```


# vuln/store32_heap-buffer-overflow.gig
## target
```
 ./gig2stereo vuln/store32_heap-buffer-overflow.gig
```

## asan report
```
==12893==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000091 at pc 0x7feda4653e61 bp 0x7fffb735b690 sp 0x7fffb735b688
WRITE of size 1 at 0x602000000091 thread T0
    #0 0x7feda4653e60 in store32(unsigned char*, unsigned int) /home/fuzzing/libgig-4.1.0/src/./helper.h:126:14
    #1 0x7feda4653e60 in DLS::Resource::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:485
    #2 0x7feda46688fa in DLS::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1700:19
    #3 0x7feda4711637 in gig::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:6345:20
    #4 0x7feda466b1be in DLS::File::Save(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1839:13
    #5 0x529d7c in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #6 0x51fea8 in main /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #7 0x7feda335f82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #8 0x41c428 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gig2stereo+0x41c428)

0x602000000091 is located 0 bytes to the right of 1-byte region [0x602000000090,0x602000000091)
allocated by thread T0 here:
    #0 0x518298 in operator new[](unsigned long) /root/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:95
    #1 0x7feda46238e0 in RIFF::Chunk::LoadChunkData() /home/fuzzing/libgig-4.1.0/src/RIFF.cpp:821:26

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fuzzing/libgig-4.1.0/src/./helper.h:126:14 in store32(unsigned char*, unsigned int)
Shadow bytes around the buggy address:
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff8000: fa fa fd fd fa fa fd fd fa fa 00 00 fa fa 00 fa
=>0x0c047fff8010: fa fa[01]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==12893==ABORTING

```


# vuln/store32_out-of-bounds-write.gig
## target
```
gig2stero vuln/store32_out-of-bounds-write.gig
```
## gdb info
```
Converting file 1/1: crashes-ste/20.gig ... 
Program received signal SIGSEGV, Segmentation fault.
store32 (data=20, pData=0x0) at helper.h:125
125	    pData[0] = data;
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]─────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x55555577f0f8 —▸ 0x7ffff7dd27b0 —▸ 0x7ffff7b68a20 (DLS::Sampler::SetGain(int)) ◂— mov    dword ptr [rdi + 0xc], esi
*RCX  0x14
*RDX  0x14
*RDI  0x20000
 RSI  0x0
*R8   0x7fffffffd800 —▸ 0x7ffff7dd1ff8 —▸ 0x7ffff7b64990 (RIFF::File::~File()) ◂— mov    rax, qword ptr [rip + 0x26e599]
 R9   0x0
 R10  0x0
*R11  0x246
*R12  0x55555577fcb0 —▸ 0x7ffff7dd1f88 —▸ 0x7ffff7b5fa70 (RIFF::Chunk::~Chunk()) ◂— mov    rax, qword ptr [rip + 0x273291]
*R13  0x55555577ed50 —▸ 0x555555781130 —▸ 0x5555557824c0 ◂— 0x55555577ed50
*R14  0x1
*R15  0x7fffffffd270 ◂— 0x0
*RBP  0x7fffffffd270 ◂— 0x0
*RSP  0x7fffffffd1b0 —▸ 0x55555577f0b0 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RIP  0x7ffff7b68c35 (DLS::Sampler::UpdateChunks(RIFF::progress_t*)+69) ◂— mov    byte ptr [rax], dl
──────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x7ffff7b68c35 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+69>     mov    byte ptr [rax], dl
   0x7ffff7b68c37 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+71>     movzx  eax, dh
   0x7ffff7b68c3a <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+74>     shr    ecx, 0x10
   0x7ffff7b68c3d <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+77>     shr    edx, 0x18
   0x7ffff7b68c40 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+80>     mov    byte ptr [r10 + 1], al
   0x7ffff7b68c44 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+84>     mov    byte ptr [r10 + 2], cl
   0x7ffff7b68c48 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+88>     mov    byte ptr [r10 + 3], dl
   0x7ffff7b68c4c <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+92>     cmp    byte ptr [rbx + 0x10], 0
   0x7ffff7b68c50 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+96>     mov    edi, dword ptr [rbx + 0x2c]
   0x7ffff7b68c53 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+99>     je     DLS::Sampler::UpdateChunks(RIFF::progress_t*)+480 <0x7ffff7b68dd0>
    ↓
   0x7ffff7b68dd0 <DLS::Sampler::UpdateChunks(RIFF::progress_t*)+480>    and    edi, 0xfffffffe
───────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────────────────────────────────────────
   120  *
   121  * @param pData - memory pointer
   122  * @param data  - integer to be stored
   123  */
   124 inline void store32(uint8_t* pData, uint32_t data) {
 ► 125     pData[0] = data;
   126     pData[1] = data >> 8;
   127     pData[2] = data >> 16;
   128     pData[3] = data >> 24;
   129 }
   130 
───────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd1b0 —▸ 0x55555577f0b0 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
01:0008│      0x7fffffffd1b8 —▸ 0x55555577fd70 —▸ 0x7ffff7dd1f88 —▸ 0x7ffff7b5fa70 (RIFF::Chunk::~Chunk()) ◂— mov    rax, qword ptr [rip + 0x273291]
02:0010│      0x7fffffffd1c0 —▸ 0x55555577f0b0 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
03:0018│      0x7fffffffd1c8 —▸ 0x7ffff7b68ef7 (DLS::Region::UpdateChunks(RIFF::progress_t*)+215) ◂— mov    rdi, qword ptr [rbx + 0x90]
04:0020│      0x7fffffffd1d0 —▸ 0x55555577f0b0 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
05:0028│      0x7fffffffd1d8 —▸ 0x55555577dc50 —▸ 0x7ffff7dd28a0 —▸ 0x7ffff7b96640 (gig::Instrument::UpdateChunks(RIFF::progress_t*)) ◂— push   r13
06:0030│      0x7fffffffd1e0 —▸ 0x7fffffffd270 ◂— 0x0
07:0038│      0x7fffffffd1e8 —▸ 0x7ffff7b9601b (gig::Region::UpdateChunks(RIFF::progress_t*)+59) ◂— mov    r9d, dword ptr [rbx + 0x130]
─────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7b68c35 DLS::Sampler::UpdateChunks(RIFF::progress_t*)+69
   f 1     7ffff7b68c35 DLS::Sampler::UpdateChunks(RIFF::progress_t*)+69
   f 2     7ffff7b68ef7 DLS::Region::UpdateChunks(RIFF::progress_t*)+215
   f 3     7ffff7b9601b gig::Region::UpdateChunks(RIFF::progress_t*)+59
   f 4     7ffff7b6950b DLS::Instrument::UpdateChunks(RIFF::progress_t*)+459
   f 5     7ffff7b96655 gig::Instrument::UpdateChunks(RIFF::progress_t*)+21
   f 6     7ffff7b69af1 DLS::File::UpdateChunks(RIFF::progress_t*)+1297
   f 7     7ffff7b96bbe gig::File::UpdateChunks(RIFF::progress_t*)+206
   f 8     7ffff7b6dfc4 DLS::File::Save(RIFF::progress_t*)+340
   f 9     55555555a6df
   f 10     55555555712c main+1820
Program received signal SIGSEGV (fault address 0x0)
```

## asan report
```
Converting file 1/1: stereo-crashes/20.gig ... AddressSanitizer:DEADLYSIGNAL
=================================================================
==59429==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f421589cc2b bp 0x000000000024 sp 0x7fff471984f0 T0)
==59429==The signal is caused by a WRITE memory access.
==59429==Hint: address points to the zero page.
    #0 0x7f421589cc2a in store32(unsigned char*, unsigned int) /home/fuzzing/libgig-4.1.0/src/./helper.h:125:14
    #1 0x7f421589cc2a in DLS::Sampler::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:607
    #2 0x7f42158a6936 in DLS::Region::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1133:18
    #3 0x7f4215912999 in gig::Region::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:3306:22
    #4 0x7f42158aa20c in DLS::Instrument::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1336:22
    #5 0x7f421593ab0d in gig::Instrument::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:4801:26
    #6 0x7f42158b133b in DLS::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1734:26
    #7 0x7f4215959637 in gig::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:6345:20
    #8 0x7f42158b31be in DLS::File::Save(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1839:13
    #9 0x529d7c in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #10 0x51fea8 in main /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #11 0x7f42145a782f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #12 0x41c428 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gig2stereo+0x41c428)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fuzzing/libgig-4.1.0/src/./helper.h:125:14 in store32(unsigned char*, unsigned int)
==59429==ABORTING

```

# vuln/store16_out-of-bounds-write.gig
## target
```
gig2stero vuln/store16_out-of-bounds-write.gig
```



## asan report
```
Converting file 1/1: stereo-crashes/22.gig ... AddressSanitizer:DEADLYSIGNAL
=================================================================
==11108==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7faade4deca2 bp 0x000000000000 sp 0x7ffcf0828fb0 T0)
==11108==The signal is caused by a WRITE memory access.
==11108==Hint: address points to the zero page.
    #0 0x7faade4deca1 in store16(unsigned char*, unsigned short) /home/fuzzing/libgig-4.1.0/src/./helper.h:114:14
    #1 0x7faade4deca1 in DLS::Region::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1160
    #2 0x7faade54a999 in gig::Region::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:3306:22
    #3 0x7faade4e220c in DLS::Instrument::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1336:22
    #4 0x7faade572b0d in gig::Instrument::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:4801:26
    #5 0x7faade4e933b in DLS::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1734:26
    #6 0x7faade591637 in gig::File::UpdateChunks(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/gig.cpp:6345:20
    #7 0x7faade4eb1be in DLS::File::Save(RIFF::progress_t*) /home/fuzzing/libgig-4.1.0/src/DLS.cpp:1839:13
    #8 0x529d7c in convertFileToStereo(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, bool, bool, bool, int) /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:388:13
    #9 0x51fea8 in main /home/fuzzing/libgig-4.1.0/src/tools/gig2stereo.cpp:661:29
    #10 0x7faadd1df82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #11 0x41c428 in _start (/home/fuzzing/libgig-4.1.0/installed/bin/gig2stereo+0x41c428)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fuzzing/libgig-4.1.0/src/./helper.h:114:14 in store16(unsigned char*, unsigned short)
==11108==ABORTING

```
## gdb info
```

1160	        store16(&pData[0], WaveLinkOptionFlags);
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]─────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x0
*RBX  0x55555577f140 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RCX  0x18360
 RDX  0x0
*RDI  0x20000
 RSI  0x0
 R8   0x0
*R9   0x55555577dce0 —▸ 0x7ffff7dd28a0 —▸ 0x7ffff7b96640 (gig::Instrument::UpdateChunks(RIFF::progress_t*)) ◂— push   r13
*R10  0x7fffffffd890 —▸ 0x7ffff7dd2940 —▸ 0x7ffff7b96af0 (gig::File::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*R11  0x246
 R12  0x0
*R13  0x55555577ede0 —▸ 0x555555781240 —▸ 0x5555557825d0 ◂— 0x55555577ede0
*R14  0x1
*R15  0x7fffffffd240 ◂— 0x0
*RBP  0xffffffff
*RSP  0x7fffffffd1a0 —▸ 0x55555577f140 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
*RIP  0x7ffff7b68f9f (DLS::Region::UpdateChunks(RIFF::progress_t*)+383) ◂— mov    byte ptr [rax], dl
──────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x7ffff7b68f9f <DLS::Region::UpdateChunks(RIFF::progress_t*)+383>    mov    byte ptr [rax], dl
   0x7ffff7b68fa1 <DLS::Region::UpdateChunks(RIFF::progress_t*)+385>    mov    byte ptr [rax + 1], sil
   0x7ffff7b68fa5 <DLS::Region::UpdateChunks(RIFF::progress_t*)+389>    movzx  edx, word ptr [rbx + 0x86]
   0x7ffff7b68fac <DLS::Region::UpdateChunks(RIFF::progress_t*)+396>    movzx  ebp, dh
   0x7ffff7b68faf <DLS::Region::UpdateChunks(RIFF::progress_t*)+399>    mov    byte ptr [rax + 2], dl
   0x7ffff7b68fb2 <DLS::Region::UpdateChunks(RIFF::progress_t*)+402>    mov    byte ptr [rax + 3], bpl
   0x7ffff7b68fb6 <DLS::Region::UpdateChunks(RIFF::progress_t*)+406>    mov    edx, dword ptr [rbx + 0x8c]
   0x7ffff7b68fbc <DLS::Region::UpdateChunks(RIFF::progress_t*)+412>    mov    r8d, edx
   0x7ffff7b68fbf <DLS::Region::UpdateChunks(RIFF::progress_t*)+415>    mov    byte ptr [rax + 4], dl
   0x7ffff7b68fc2 <DLS::Region::UpdateChunks(RIFF::progress_t*)+418>    mov    byte ptr [rax + 5], dh
   0x7ffff7b68fc5 <DLS::Region::UpdateChunks(RIFF::progress_t*)+421>    shr    r8d, 0x10
───────────────────────────────────────────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────────────────────────────────────────
   1153                     index = i;
   1154                     break;
   1155                 }
   1156             }
   1157         }
 ► 1158         WavePoolTableIndex = index;
   1159         // update 'wlnk' chunk
   1160         store16(&pData[0], WaveLinkOptionFlags);
   1161         store16(&pData[2], PhaseGroup);
   1162         store32(&pData[4], Channel);
   1163         store32(&pData[8], WavePoolTableIndex);
───────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rsp  0x7fffffffd1a0 —▸ 0x55555577f140 —▸ 0x7ffff7dd2738 —▸ 0x7ffff7b95fe0 (gig::Region::UpdateChunks(RIFF::progress_t*)) ◂— push   r15
01:0008│      0x7fffffffd1a8 —▸ 0x55555577dce0 —▸ 0x7ffff7dd28a0 —▸ 0x7ffff7b96640 (gig::Instrument::UpdateChunks(RIFF::progress_t*)) ◂— push   r13
02:0010│      0x7fffffffd1b0 —▸ 0x7fffffffd240 ◂— 0x0
03:0018│      0x7fffffffd1b8 —▸ 0x7ffff7b9601b (gig::Region::UpdateChunks(RIFF::progress_t*)+59) ◂— mov    r9d, dword ptr [rbx + 0x130]
04:0020│      0x7fffffffd1c0 —▸ 0x7fffffffd320 ◂— 0x0
05:0028│      0x7fffffffd1c8 —▸ 0x55555577db80 —▸ 0x5555557825f0 ◂— 0x55555577db80
06:0030│      0x7fffffffd1d0 —▸ 0x5555557825f0 —▸ 0x55555577db80 ◂— 0x5555557825f0
07:0038│      0x7fffffffd1d8 —▸ 0x7ffff72380fc (malloc+140) ◂— test   rax, rax
─────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0     7ffff7b68f9f DLS::Region::UpdateChunks(RIFF::progress_t*)+383
   f 1     7ffff7b9601b gig::Region::UpdateChunks(RIFF::progress_t*)+59
   f 2     7ffff7b6950b DLS::Instrument::UpdateChunks(RIFF::progress_t*)+459
   f 3     7ffff7b96655 gig::Instrument::UpdateChunks(RIFF::progress_t*)+21
   f 4     7ffff7b69af1 DLS::File::UpdateChunks(RIFF::progress_t*)+1297
   f 5     7ffff7b96bbe gig::File::UpdateChunks(RIFF::progress_t*)+206
   f 6     7ffff7b6dfc4 DLS::File::Save(RIFF::progress_t*)+340
   f 7     55555555a6df
   f 8     55555555712c main+1820
   f 9     7ffff71c2b97 __libc_start_main+231

```
