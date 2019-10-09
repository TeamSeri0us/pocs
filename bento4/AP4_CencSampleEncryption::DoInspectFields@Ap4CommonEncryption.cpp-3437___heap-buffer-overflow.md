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

## AP4_CencSampleEncryption::DoInspectFields@Ap4CommonEncryption.cpp-3437___heap-buffer-overflow

### description

    An issue was discovered in bento4 1.5.1.0, There is a/an heap-buffer-overflow in function AP4_CencSampleEncryption::DoInspectFields at Ap4CommonEncryption.cpp-3437

### commandline

    mp4dump --verbosity 2 @@

### source

```c
3433             info += 2;
3434             for (unsigned int j=0; j<num_entries; j++) {
3435                 unsigned int bocd = AP4_BytesToUInt16BE(info);
3436                 AP4_FormatString(header, sizeof(header), "sub-entry %04d.%d bytes of clear data", i, j);
3437                 inspector.AddField(header, bocd);
3438                 unsigned int boed = AP4_BytesToUInt32BE(info+2);
3439                 AP4_FormatString(header, sizeof(header), "sub-entry %04d.%d bytes of encrypted data", i, j);
3440                 inspector.AddField(header, boed);
3441                 info += 6;
3442             }

```

### bug report

```txt
=================================================================
==20093==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61300000dfee at pc 0x00000060256b bp 0x7ffdb67cdb90 sp 0x7ffdb67cdb80
READ of size 4 at 0x61300000dfee thread T0
    #0 0x60256a in AP4_CencSampleEncryption::DoInspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4CommonEncryption.cpp:3437
    #1 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #2 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #3 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #4 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #5 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #6 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #7 0x58b005 in AP4_AtomListInspector::Action(AP4_Atom*) const /src/bento4/Source/C++/Core/Ap4Atom.h:530
    #8 0x58b005 in AP4_List<AP4_Atom>::Apply(AP4_List<AP4_Atom>::Item::Operator const&) const /src/bento4/Source/C++/Core/Ap4List.h:353
    #9 0x58b005 in AP4_ContainerAtom::InspectChildren(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:220
    #10 0x58b005 in AP4_ContainerAtom::InspectFields(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4ContainerAtom.cpp:210
    #11 0x4d3dae in AP4_Atom::Inspect(AP4_AtomInspector&) /src/bento4/Source/C++/Core/Ap4Atom.cpp:263
    #12 0x43f769 in main /src/bento4/Source/C++/Apps/Mp4Dump/Mp4Dump.cpp:350
    #13 0x7f7d03b2b82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #14 0x4434e8 in _start (/src/aflbuild/installed/bin/mp4dump+0x4434e8)

0x61300000dfee is located 0 bytes to the right of 366-byte region [0x61300000de80,0x61300000dfee)
allocated by thread T0 here:
    #0 0x7f7d045066b2 in operator new[](unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x996b2)
    #1 0x536f2f in AP4_DataBuffer::ReallocateBuffer(unsigned int) /src/bento4/Source/C++/Core/Ap4DataBuffer.cpp:210
    #2 0x536f2f in AP4_DataBuffer::SetDataSize(unsigned int) /src/bento4/Source/C++/Core/Ap4DataBuffer.cpp:151

SUMMARY: AddressSanitizer: heap-buffer-overflow /src/bento4/Source/C++/Core/Ap4CommonEncryption.cpp:3437 AP4_CencSampleEncryption::DoInspectFields(AP4_AtomInspector&)
Shadow bytes around the buggy address:
  0x0c267fff9ba0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff9bb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff9bc0: 00 00 00 00 00 00 00 00 fa fa fa fa fa fa fa fa
  0x0c267fff9bd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff9be0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c267fff9bf0: 00 00 00 00 00 00 00 00 00 00 00 00 00[06]fa fa
  0x0c267fff9c00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff9c10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff9c20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff9c30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff9c40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==20093==ABORTING

```

### others

    from fuzz project pwd-bento4-mp4dump-02
    crash name pwd-bento4-mp4dump-02-00000034-20190811.mp4
    Auto-generated by pyspider at 2019-08-11 19:37:41
    
    please send email to  teamseri0us360@gmail.com if you have any questions.

