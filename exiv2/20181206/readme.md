# description
Exiv2 is a C++ library and a command line utility to read, write, delete and modify Exif, IPTC, XMP and ICC image metadata.

# version
0.27-RC2

# others
## @_@

This bug is reported by fish@360TeamSeri0us, please send email to  teamSeri0us360@gmail.com if you have any questions.

# details


1.fish@ubuntu:~/Desktop/2018-10-10/image/exiv2$ ./exiv2 -pR pngimage-heap-bof-poc-1

```
STRUCTURE OF PNG FILE: pngimage-heap-bof-poc-1
 address | chunk |  length | data                           | checksum
       8 | tEXt  |      13 | ... ... ....                   | 0x44a48ac6
      33 | tEXt  |      25 | Software.Adobe ImageReady      | 0x71c9653c
=================================================================
==113281==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6030000009ba at pc 0x7f4af3fd811d bp 0x7ffd47126490 sp 0x7ffd47126480
READ of size 1 at 0x6030000009ba thread T0
    #0 0x7f4af3fd811c in tEXtToDataBuf /home/fish/Desktop/2018-10-10/image/exiv2/src/pngimage.cpp:178
    #1 0x7f4af3fd811c in Exiv2::PngImage::printStructure(std::ostream&, Exiv2::PrintStructureOption, int) /home/fish/Desktop/2018-10-10/image/exiv2/src/pngimage.cpp:331
    #2 0x557cf0232702 in printStructure /home/fish/Desktop/2018-10-10/image/exiv2/src/actions.cpp:2361
    #3 0x557cf026ff6c in Action::Print::run(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) /home/fish/Desktop/2018-10-10/image/exiv2/src/actions.cpp:251
    #4 0x557cf01dd1dd in main /home/fish/Desktop/2018-10-10/image/exiv2/src/exiv2.cpp:169
    #5 0x7f4af2f8ab96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #6 0x557cf01de369 in _start (/home/fish/Desktop/2018-10-10/image/exiv2/afl/afl/bin/exiv2+0x14369)

0x6030000009ba is located 0 bytes to the right of 26-byte region [0x6030000009a0,0x6030000009ba)
allocated by thread T0 here:
    #0 0x7f4af4b1a618 in operator new[](unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xe0618)
    #1 0x7f4af3fd2934 in Exiv2::PngImage::printStructure(std::ostream&, Exiv2::PrintStructureOption, int) /home/fish/Desktop/2018-10-10/image/exiv2/src/pngimage.cpp:320

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/image/exiv2/src/pngimage.cpp:178 in tEXtToDataBuf
Shadow bytes around the buggy address:
  0x0c067fff80e0: fd fd fd fd fa fa 00 00 00 07 fa fa fd fd fd fd
  0x0c067fff80f0: fa fa fd fd fd fd fa fa fd fd fd fd fa fa fd fd
  0x0c067fff8100: fd fd fa fa fd fd fd fd fa fa fd fd fd fd fa fa
  0x0c067fff8110: fd fd fd fd fa fa fd fd fd fd fa fa fd fd fd fd
  0x0c067fff8120: fa fa fd fd fd fd fa fa fd fd fd fd fa fa fd fd
=>0x0c067fff8130: fd fd fa fa 00 00 00[02]fa fa fa fa fa fa fa fa
  0x0c067fff8140: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8150: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8160: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8170: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8180: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==113281==ABORTING

```


2.fish@ubuntu:~/Desktop/2018-10-10/image/exiv2/data/poc$ ./exiv2 -Y 2011 -O 02 -D 29 adjust tiffimage_int-out-of-bound-read-poc-2

```
m1-26f459b3eb2a285626b849d6950db7ab.tif
Error: Directory Image: Next pointer is out of bounds; ignored.
Error: Directory Image, entry 0x00fe has invalid size 1358954497*4; skipping entry.
Error: Directory Image, entry 0x011b has invalid size 1107296257*8; skipping entry.
Error: XMP Toolkit error 201: XML parsing failure
Warning: Failed to decode XMP metadata.
Error: Directory Image: Next pointer is out of bounds; ignored.
Error: Directory Image, entry 0x00fe has invalid size 1358954497*4; skipping entry.
Error: Directory Image, entry 0x011b has invalid size 1107296257*8; skipping entry.
ASAN:DEADLYSIGNAL
=================================================================
==24291==ERROR: AddressSanitizer: SEGV on unknown address 0x00000000000c (pc 0x7fe6e2891e78 bp 0x7ffed602d560 sp 0x7ffed602d440 T0)
==24291==The signal is caused by a READ memory access.
==24291==Hint: address points to the zero page.
    #0 0x7fe6e2891e77 in Exiv2::Internal::TiffParserWorker::findPrimaryGroups(std::vector<Exiv2::Internal::IfdId, std::allocator<Exiv2::Internal::IfdId> >&, Exiv2::Internal::TiffComponent*) /home/fish/Desktop/2018-10-10/image/exiv2/src/tiffimage_int.cpp:1698
    #1 0x7fe6e2895d24 in Exiv2::Internal::TiffParserWorker::encode(Exiv2::BasicIo&, unsigned char const*, unsigned int, Exiv2::ExifData const&, Exiv2::IptcData const&, Exiv2::XmpData const&, unsigned int, void (Exiv2::Internal::TiffEncoder::*(*)(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, Exiv2::Internal::IfdId))(Exiv2::Internal::TiffEntryBase*, Exiv2::Exifdatum const*), Exiv2::Internal::TiffHeaderBase*, Exiv2::Internal::OffsetWriter*) /home/fish/Desktop/2018-10-10/image/exiv2/src/tiffimage_int.cpp:1592
    #2 0x7fe6e2536540 in Exiv2::TiffParser::encode(Exiv2::BasicIo&, unsigned char const*, unsigned int, Exiv2::ByteOrder, Exiv2::ExifData const&, Exiv2::IptcData const&, Exiv2::XmpData const&) /home/fish/Desktop/2018-10-10/image/exiv2/src/tiffimage.cpp:305
    #3 0x7fe6e25458dd in Exiv2::TiffImage::writeMetadata() /home/fish/Desktop/2018-10-10/image/exiv2/src/tiffimage.cpp:248
    #4 0x563b37a5a0fa in Action::Adjust::run(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) /home/fish/Desktop/2018-10-10/image/exiv2/src/actions.cpp:1677
    #5 0x563b3799f1dd in main /home/fish/Desktop/2018-10-10/image/exiv2/src/exiv2.cpp:169
    #6 0x7fe6e15feb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #7 0x563b379a0369 in _start (/home/fish/Desktop/2018-10-10/image/exiv2/afl/afl/bin/exiv2+0x14369)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/2018-10-10/image/exiv2/src/tiffimage_int.cpp:1698 in Exiv2::Internal::TiffParserWorker::findPrimaryGroups(std::vector<Exiv2::Internal::IfdId, std::allocator<Exiv2::Internal::IfdId> >&, Exiv2::Internal::TiffComponent*)
==24291==ABORTING

```

3.fish@ubuntu:~/Desktop/2018-10-10/image/exiv2/data/poc$ ./exiv2 -M'set Xmp.dc.title lang="de-DE" Euros' jp2image-heap-bof-poc-3


```
=================================================================
==128911==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6030000005f4 at pc 0x7ff6ac1a6733 bp 0x7ffded608850 sp 0x7ffded607ff8
READ of size 1785737760 at 0x6030000005f4 thread T0
    #0 0x7ff6ac1a6732  (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x79732)
    #1 0x7ff6ab46e9d7 in Exiv2::Jp2Image::encodeJp2Header(Exiv2::DataBuf const&, Exiv2::DataBuf&) /home/fish/Desktop/2018-10-10/image/exiv2/src/jp2image.cpp:676
    #2 0x7ff6ab470e94 in Exiv2::Jp2Image::doWriteMetadata(Exiv2::BasicIo&) /home/fish/Desktop/2018-10-10/image/exiv2/src/jp2image.cpp:787
    #3 0x7ff6ab47c4f9 in Exiv2::Jp2Image::writeMetadata() /home/fish/Desktop/2018-10-10/image/exiv2/src/jp2image.cpp:610
    #4 0x55668dd4b9d8 in Action::Modify::run(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) /home/fish/Desktop/2018-10-10/image/exiv2/src/actions.cpp:1428
    #5 0x55668dc961dd in main /home/fish/Desktop/2018-10-10/image/exiv2/src/exiv2.cpp:169
    #6 0x7ff6aa67db96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #7 0x55668dc97369 in _start (/home/fish/Desktop/2018-10-10/image/exiv2/afl/afl/bin/exiv2+0x14369)

0x6030000005f4 is located 0 bytes to the right of 20-byte region [0x6030000005e0,0x6030000005f4)
allocated by thread T0 here:
    #0 0x7ff6ac20d618 in operator new[](unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xe0618)
    #1 0x7ff6ab5c8aeb in Exiv2::DataBuf::DataBuf(long) /home/fish/Desktop/2018-10-10/image/exiv2/src/types.cpp:141
    #2 0x7ffded608be7  (<unknown module>)

SUMMARY: AddressSanitizer: heap-buffer-overflow (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x79732) 
Shadow bytes around the buggy address:
  0x0c067fff8060: fa fa 00 00 00 00 fa fa 00 00 00 00 fa fa fd fd
  0x0c067fff8070: fd fa fa fa fd fd fd fd fa fa fd fd fd fa fa fa
  0x0c067fff8080: fd fd fd fd fa fa fd fd fd fa fa fa fd fd fd fd
  0x0c067fff8090: fa fa fd fd fd fd fa fa fd fd fd fd fa fa 00 00
  0x0c067fff80a0: 03 fa fa fa 00 00 00 fa fa fa fd fd fd fa fa fa
=>0x0c067fff80b0: fd fd fd fa fa fa 00 00 00 fa fa fa 00 00[04]fa
  0x0c067fff80c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff80d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff80e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff80f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8100: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==128911==ABORTING

```

4.fish@ubuntu:~/Desktop/2018-10-10/image/exiv2/data/poc$ ./iptcprint abort-poc-4

```
terminate called after throwing an instance of 'std::overflow_error'
  what():  Overflow in addition
Aborted
```

5.fish@ubuntu:~/Desktop/2018-10-10/image/exiv2/data/poc$ ./exiv2 insert jp2image-infiniteloop-poc-5
^C

```
  629	         int32_t       count  = sizeof (Jp2BoxHeader);
    630	         char*         p      = (char*) boxBuf.pData_;
    631	         bool          bWroteColor = false ;
    632	 
    633	         while ( count < length || !bWroteColor ) {
		// pSubBox=0x00007fffffffb538  →  [...]  →  0x01726c6f00000000, p=0x00007fffffffb530  →  [...]  →  0x6832706a2d000000
 →  634	             Jp2BoxHeader* pSubBox = (Jp2BoxHeader*) (p+count) ;
    635	 
    636	             // copy data.  pointer could be into a memory mapped file which we will decode!
    637	             Jp2BoxHeader   subBox = *pSubBox ;
    638	             Jp2BoxHeader   newBox =  subBox;
    639	 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "exiv2", stopped, reason: SINGLE STEP
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff798bb95 → Name: Exiv2::Jp2Image::encodeJp2Header(this=0x5555557bb650, boxBuf=@0x7fffffffb5d0, outBuf=@0x7fffffffb5e0)
[#1] 0x7ffff798c474 → Name: Exiv2::Jp2Image::doWriteMetadata(this=0x5555557bb650, outIo=@0x5555557e7d10)
[#2] 0x7ffff798b9d0 → Name: Exiv2::Jp2Image::writeMetadata(this=0x5555557bb650)
[#3] 0x555555585650 → Name: (anonymous namespace)::metacopy(source="jp2image-infiniteloop-poc-5.exv", tgt="", targetType=0x0, preserve=0x1)
[#4] 0x55555557f315 → Name: Action::Insert::run(this=0x5555557b3270, path="jp2image-infiniteloop-poc-5")
[#5] 0x555555567452 → Name: main(argc=0x3, argv=0x7fffffffddc8)
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
634	            Jp2BoxHeader* pSubBox = (Jp2BoxHeader*) (p+count) ;
gef➤  p subBox
$2 = {
  length = 0x0, 
  type = 0x6f6c7201
}

```



	
