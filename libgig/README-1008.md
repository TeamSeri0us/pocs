# Description

libgig is a C++ library for loading, modifying existing and creating new Gigasampler (.gig) files and DLS (Downloadable Sounds) Level 1/2 files, KORG sample based instruments (.KSF and .KMP files), SoundFont v2 (.sf2) files and AKAI sampler data. The source code package includes a couple of command line tools based on the library. The library and tools are released in source code format under the GNU General Public License, except the AKAI classes which are released under the GNU Lesser General Public License.

# version

libgig 4.1.0

# others

## @_@
this bug is reported by pwd@360TeamSeri0us,
please send email to  teamSeri0us360@gmail.com if you have any question.
pocs is in vuln-1008

# Detial

## heap-buffer-overflow_RIFF.cpp:1536:32

### target

./rifftree --first-chunk-id RIFF --flat vuln-1008/heap-buffer-overflow_RIFF.cpp:1536:32

An issue was discovered in libgig 4.1.0. There is a heap-buffer-overflow in the  RIFF::List::GetListTypeString[abi:cxx11]() const at src/RIFF.cpp:1536:32.

### asan report

```txt
Flat RIFF-alike file
=================================================================
==17330==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x607000007930 at pc 0x7f53716da4b6 bp 0x7ffec161f290 sp 0x7ffec161f288
READ of size 4 at 0x607000007930 thread T0
    #0 0x7f53716da4b5 in RIFF::List::GetListTypeString[abi:cxx11]() const /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1536:32
    #1 0x51f831 in PrintChunkList(RIFF::List*, bool) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/rifftree.cpp:155:35
    #2 0x51a641 in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/rifftree.cpp:127:9
    #3 0x7f537033bb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #4 0x41b509 in _start (/home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed-asan/bin/rifftree+0x41b509)

0x607000007930 is located 0 bytes to the right of 80-byte region [0x6070000078e0,0x607000007930)
allocated by thread T0 here:
    #0 0x513970 in operator new(unsigned long) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:92
    #1 0x7f53716d2061 in RIFF::List::LoadSubChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1451:26
    #2 0x7f53716dbfc4 in RIFF::File::__openExistingFile(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1706:17
    #3 0x7f53716df84e in RIFF::File::File(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, RIFF::endian_t, RIFF::layout_t, RIFF::offset_size_t) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1638:13
    #4 0x51a299 in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/rifftree.cpp:119:28
    #5 0x7f537033bb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1536:32 in RIFF::List::GetListTypeString[abi:cxx11]() const
Shadow bytes around the buggy address:
  0x0c0e7fff8ed0: 00 fa fa fa fa fa 00 00 00 00 00 00 00 00 00 fa
  0x0c0e7fff8ee0: fa fa fa fa 00 00 00 00 00 00 00 00 00 fa fa fa
  0x0c0e7fff8ef0: fa fa 00 00 00 00 00 00 00 00 00 fa fa fa fa fa
  0x0c0e7fff8f00: 00 00 00 00 00 00 00 00 00 fa fa fa fa fa 00 00
  0x0c0e7fff8f10: 00 00 00 00 00 00 00 fa fa fa fa fa 00 00 00 00
=>0x0c0e7fff8f20: 00 00 00 00 00 00[fa]fa fa fa fa fa fa fa fa fa
  0x0c0e7fff8f30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0e7fff8f40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0e7fff8f50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0e7fff8f60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0e7fff8f70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==17330==ABORTING
```

## out-of-bounds-read_DLS.cpp:1515:14

### target

./dlsdump vuln-1008/out-of-bounds-read_DLS.cpp:1515:14

An issue was discovered in libgig 4.1.0. There is an out-of-bounds read in the function DLS::File::GetFirstSample() at src/DLS.cpp:1515:14.

### asan report

```txt
File Name: "GAO-SHENG   "
ALL Available Samples (as there might be more than referenced by Instruments):

Available Instruments:
    Instrument 1) "GAO-SHENG   ",  MIDIBank=0, MIDIProgram=0
AddressSanitizer:DEADLYSIGNAL
=================================================================
==17934==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f856d3f625b bp 0x60f000000d10 sp 0x7fff673a68d0 T0)
==17934==The signal is caused by a READ memory access.
==17934==Hint: address points to the zero page.
    #0 0x7f856d3f625a in DLS::File::GetFirstSample() /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1515:14
    #1 0x7f856d3f625a in DLS::Region::GetSample() /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1053
    #2 0x51e519 in PrintRegions(DLS::Instrument*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:126:41
    #3 0x51dcbc in PrintInstruments(DLS::File*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:113:9
    #4 0x518afe in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:70:9
    #5 0x7f856c02bb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41b7b9 in _start (/home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed-asan/bin/dlsdump+0x41b7b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1515:14 in DLS::File::GetFirstSample()
==17934==ABORTING

```

### source code

```c
   1049     Sample* Region::GetSample() {
   1050         if (pSample) return pSample;
   1051         File* file = (File*) GetParent()->GetParent();
 ► 1052         uint64_t soughtoffset = file->pWavePoolTable[WavePoolTableIndex];
   1053         Sample* sample = file->GetFirstSample();
   1054         while (sample) {
   1055             if (sample->ullWavePoolOffset == soughtoffset) return (pSample = sample);
   1056             sample = file->GetNextSample();
   1057         }

```

## operator-new-failed_DLS.cpp:570:51

### target

./dlsdump vuln-1008/operator-new-failed_DLS.cpp\:570\:51

An issue was discovered in libgig 4.1.0. There is an operator new[] failed (due to a big heap request) in DLS::Sampler::Sampler(RIFF::List*) at src/DLS.cpp:570:51.

### source code

```c

   565             SamplerOptions = F_WSMP_NO_COMPRESSION;
   566             SampleLoops    = 0;
   567         }
   568         NoSampleDepthTruncation = SamplerOptions & F_WSMP_NO_TRUNCATION;
   569         NoSampleCompression     = SamplerOptions & F_WSMP_NO_COMPRESSION;
 ► 570         pSampleLoops            = (SampleLoops) ? new sample_loop_t[SampleLoops] : NULL;
   571         if (SampleLoops) {
   572             wsmp->SetPos(uiHeaderSize);
   573             for (uint32_t i = 0; i < SampleLoops; i++) {
   574                 wsmp->Read(pSampleLoops + i, 4, 4);
   575                 if (pSampleLoops[i].Size > sizeof(sample_loop_t)) { // if loop struct was extended

//  pwndbg> p SampleLoops
//  $4 = 2147483649
```

## heap-buffer-overflow_DLS.cpp:1052:33

### target 

./dlsdump vuln-1008/heap-buffer-overflow_DLS.cpp:1052:33

An issue was discovered in libgig 4.1.0. There is a heap-buffer-overflow in DLS::Region::GetSample() at src/DLS.cpp:1052:33.

### asan report 

```txt
File Name: "GAO-SHENG   "
ALL Available Samples (as there might be more than referenced by Instruments):
    Sample 1) "GH1         ", 44100Hz, 1 Channels
    Sample 2) "GH2         ", 44100Hz, 1 Channels
    Sample 3) "GH3         ", 44100Hz, 1 Channels
    Sample 4) "GH4         ", 44100Hz, 1 Channels
    Sample 5) "GH5         ", 44100Hz, 1 Channels
    Sample 6) "GH6         ", 44100Hz, 1 Channels

Available Instruments:
    Instrument 1) "GAO-SHENG   ",  MIDIBank=0, MIDIProgram=0
        Region 1) Sample: "GH1         ", 44100Hz, KeyRange=55-60, VelocityRange=0-127, Layer=0
            Loops=1
=================================================================
==19983==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x603000004714 at pc 0x7f35e0e6c5fa bp 0x7ffe03b5c360 sp 0x7ffe03b5c358
READ of size 4 at 0x603000004714 thread T0
    #0 0x7f35e0e6c5f9 in DLS::Region::GetSample() /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1052:33
    #1 0x51e519 in PrintRegions(DLS::Instrument*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:126:41
    #2 0x51dcbc in PrintInstruments(DLS::File*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:113:9
    #3 0x518afe in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:70:9
    #4 0x7f35dfaa1b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41b7b9 in _start (/home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed-asan/bin/dlsdump+0x41b7b9)

0x603000004714 is located 12 bytes to the left of 24-byte region [0x603000004720,0x603000004738)
allocated by thread T0 here:
    #0 0x513c20 in operator new(unsigned long) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_new_delete.cc:92
    #1 0x7f35e0e382a9 in __gnu_cxx::new_allocator<std::_List_node<RIFF::Chunk*> >::allocate(unsigned long, void const*) /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/ext/new_allocator.h:111:27
    #2 0x7f35e0e382a9 in std::allocator_traits<std::allocator<std::_List_node<RIFF::Chunk*> > >::allocate(std::allocator<std::_List_node<RIFF::Chunk*> >&, unsigned long) /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/bits/alloc_traits.h:436
    #3 0x7f35e0e382a9 in std::__cxx11::_List_base<RIFF::Chunk*, std::allocator<RIFF::Chunk*> >::_M_get_node() /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/bits/stl_list.h:383
    #4 0x7f35e0e382a9 in std::_List_node<RIFF::Chunk*>* std::__cxx11::list<RIFF::Chunk*, std::allocator<RIFF::Chunk*> >::_M_create_node<RIFF::Chunk* const&>(RIFF::Chunk* const&) /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/bits/stl_list.h:572
    #5 0x7f35e0e382a9 in void std::__cxx11::list<RIFF::Chunk*, std::allocator<RIFF::Chunk*> >::_M_insert<RIFF::Chunk* const&>(std::_List_iterator<RIFF::Chunk*>, RIFF::Chunk* const&) /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/bits/stl_list.h:1801
    #6 0x7f35e0e382a9 in std::__cxx11::list<RIFF::Chunk*, std::allocator<RIFF::Chunk*> >::push_back(RIFF::Chunk* const&) /usr/lib/gcc/x86_64-linux-gnu/7.3.0/../../../../include/c++/7.3.0/bits/stl_list.h:1118
    #7 0x7f35e0e382a9 in RIFF::List::LoadSubChunks(RIFF::progress_t*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1454
    #8 0x7f35e0e38d30 in RIFF::List::GetSubList(unsigned int) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/RIFF.cpp:1094:26

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1052:33 in DLS::Region::GetSample()
Shadow bytes around the buggy address:
  0x0c067fff8890: 00 00 00 fa fa fa fd fd fd fd fa fa 00 00 00 07
  0x0c067fff88a0: fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00
  0x0c067fff88b0: 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa
  0x0c067fff88c0: 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa
  0x0c067fff88d0: fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00
=>0x0c067fff88e0: 00 fa[fa]fa 00 00 00 fa fa fa 00 00 00 fa fa fa
  0x0c067fff88f0: 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa
  0x0c067fff8900: fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00
  0x0c067fff8910: 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa
  0x0c067fff8920: 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00 00 fa
  0x0c067fff8930: fa fa 00 00 00 fa fa fa 00 00 00 fa fa fa 00 00
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
==19983==ABORTING
```

## operator-new-failed_DLS.cpp:1462

### target

./dlsdump vuln-1008/operator-new-failed_DLS.cpp:570:51
An issue was discovered in libgig 4.1.0. There is an operator new[] failed (due to a big heap request) in DLS::File::File at DLS.cpp:1462.

### source code

```c
   1457             WavePoolHeaderSize = 8;
   1458             b64BitWavePoolOffsets = false;
   1459         } else {
   1460             WavePoolHeaderSize = ptbl->ReadUint32();
   1461             WavePoolCount  = ptbl->ReadUint32();
 ► 1462             pWavePoolTable = new uint32_t[WavePoolCount];
   1463             pWavePoolTableHi = new uint32_t[WavePoolCount];
   1464             ptbl->SetPos(WavePoolHeaderSize);
   1465
   1466             // Check for 64 bit offsets (used in gig v3 files)
   1467             b64BitWavePoolOffsets = (ptbl->GetSize() - WavePoolHeaderSize == WavePoolCount * 8);


//  pwndbg> p WavePoolCount 
//  $2 = 2147483654
```

## FPE-on-unknown-address_DLS.cpp:743:92

### target

./dlsdump vuln-1008/FPE-on-unknown-address_DLS.cpp:743:92
An issue discovered in libgig 4.1.0. There is a FPE on unknown address in DLS::Sample::Sample at DLS.cpp:743:92.

### asan report

```txt
File Name: "GAO-SHENG   "
ALL Available Samples (as there might be more than referenced by Instruments):
AddressSanitizer:DEADLYSIGNAL
=================================================================
==22032==ERROR: AddressSanitizer: FPE on unknown address 0x7efdfee76356 (pc 0x7efdfee76356 bp 0x000000000002 sp 0x7ffce5cb2170 T0)
    #0 0x7efdfee76355 in DLS::Sample::Sample(DLS::File*, RIFF::List*, unsigned long) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:743:92
    #1 0x7efdfee85c7b in DLS::File::LoadSamples() /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1536:45
    #2 0x7efdfee7c749 in DLS::File::GetFirstSample() /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:1515:24
    #3 0x51b54c in PrintSamples(DLS::File*) /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:89:33
    #4 0x5188d2 in main /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/tools/dlsdump.cpp:68:9
    #5 0x7efdfdab1b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41b7b9 in _start (/home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/installed-asan/bin/dlsdump+0x41b7b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: FPE /home/pwd/fuzz/from_exploit/libgig/libgig-4.1.0/src/DLS.cpp:743:92 in DLS::Sample::Sample(DLS::File*, RIFF::List*, unsigned long)
==22032==ABORTING
```

### source code

```c
 ► 743         SamplesTotal = (pCkData) ? (FormatTag == DLS_WAVE_FORMAT_PCM) ? pCkData->GetSize() / FrameSize
   744                                                                       : 0
   745                                  : 0;
//  pwndbg> p FrameSize
//  $1 = 0
//  ERROR: div 0
```
