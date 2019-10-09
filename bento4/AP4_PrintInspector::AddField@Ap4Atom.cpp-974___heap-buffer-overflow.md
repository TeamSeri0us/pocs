# bento4

## version 

    bento4 1.5.1.0

## description

```txt
None
```

## download link

    None

## others

    please send email to  teamseri0us360@gmail.com if you have any questions.

---------------------

## AP4_PrintInspector::AddField@Ap4Atom.cpp-974___heap-buffer-overflow

### description

    An issue was discovered in bento4 1.5.1.0, There is a/an heap-buffer-overflow in function AP4_PrintInspector::AddField at Ap4Atom.cpp-974

### commandline

    mp4dump --verbosity 2 @@

### source

```c
 970     m_Stream->WriteString(" = [");
 971     unsigned int offset = 1;
 972     char byte[4];
 973     for (unsigned int i=0; i<byte_count; i++) {
 974         AP4_FormatString(byte, 4, " %02x", bytes[i]);
 975         m_Stream->Write(&byte[offset], 3-offset);
 976         offset = 0;
 977     }
 978     m_Stream->Write("]\n", 2);
 979 }

```

### bug report

```txt
=================================================================
==4107==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x611000009d76 at pc 0x0000004dcdcb bp 0x7ffc9fc51e20 sp 0x7ffc9fc51e10
READ of size 1 at 0x611000009d76 thread T0
    #0 0x4dcdca in AP4_PrintInspector::AddField(char const*, unsigned char const*, unsigned int, AP4_AtomInspector::FormatHint) /src/bento4/Source/C++/Core/Ap4Atom.cpp:974
    #1 0x601dab in AP4_CencSampleEncryption::DoInspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4CommonEncryption.cpp:3429
    #2 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #3 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #4 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #5 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #6 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #7 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #8 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #9 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #10 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #11 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #12 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #13 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #14 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #15 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #16 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #17 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #18 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #19 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #20 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #21 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #22 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #23 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #24 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #25 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #26 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #27 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #28 0x43f769 in main /src/bento4/Source/C++/Apps/Mp4Dump/Mp4Dump.cpp:350
    #29 0x7f160934782f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #30 0x4434e8 in _start (/src/aflbuild/installed/bin/mp4dump+0x4434e8)

0x611000009d76 is located 0 bytes to the right of 246-byte region [0x611000009c80,0x611000009d76)
allocated by thread T0 here:
    #0 0x7f1609d226b2 in operator new[](unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x996b2)
    #1 0x536f2f in AP4_DataBuffer::ReallocateBuffer(unsigned int) /src/bento4/Source/C++/Core/Ap4DataBuffer.cpp:210
    #2 0x536f2f in AP4_DataBuffer::SetDataSize(unsigned int) /src/bento4/Source/C++/Core/Ap4DataBuffer.cpp:151

SUMMARY: AddressSanitizer: heap-buffer-overflow /src/bento4/Source/C++/Core/Ap4Atom.cpp:974 AP4_PrintInspector::AddField(char const*, unsigned char const*, unsigned int, AP4_AtomInspector::FormatHint)
Shadow bytes around the buggy address:
  0x0c227fff9350: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c227fff9360: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c227fff9370: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c227fff9380: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c227fff9390: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c227fff93a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00[06]fa
  0x0c227fff93b0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c227fff93c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c227fff93d0: 00 00 00 00 00 00 00 00 fa fa fa fa fa fa fa fa
  0x0c227fff93e0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c227fff93f0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
==4107==ABORTING

```

### others

    from fuzz project pwd-bento4-mp4dump-02
    crash name pwd-bento4-mp4dump-02-00000029-20190811.mp4
    Auto-generated by pyspider at 2019-08-11 11:06:47
    
    please send email to  teamseri0us360@gmail.com if you have any questions.