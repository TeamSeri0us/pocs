## Description

FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.

## Version

[2.8.1](https://github.com/knik0/faad2/archive/2_8_1.tar.gz)

## Others

this bug is reported by fish@360TeamSeri0us, 
please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details

1. There was a buffer-overflow problem in function parse() in frontend/mp4read.c:746.

```	
fish@ubuntu: ./afl/afl/bin/faad global-buffer-overflow-1
 *********** Ahead Software MPEG-4 AAC Decoder V2.8.8 ******************

 Build: Nov 11 2018
 Copyright 2002-2004: Ahead Software AG
 http://www.audiocoding.com
 bug tracking: https://sourceforge.net/p/faac/bugs/
 Floating point version

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License.

 **************************************************************************

**** MP4 header ****
Brand:			mp42(version 0)
Compatible brands:	mp42isom
*track media type: 'soun': OK
=================================================================
==73817==ERROR: AddressSanitizer: global-buffer-overflow on address 0x56118d728230 at pc 0x56118d4fdb1d bp 0x7ffd93a74c40 sp 0x7ffd93a74c30
READ of size 2 at 0x56118d728230 thread T0
    #0 0x56118d4fdb1c in parse ../../frontend/mp4read.c:746
    #1 0x56118d505ce2 in mp4read_open ../../frontend/mp4read.c:991
    #2 0x56118d517624 in decodeMP4file ../../frontend/main.c:830
    #3 0x56118d517624 in faad_main ../../frontend/main.c:1308
    #4 0x7f4a23581b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #5 0x56118d4fce69 in _start (/home/fish/Desktop/2018-10-10/sound_audio/faad2/afl/afl/bin/faad+0xae69)

0x56118d728230 is located 48 bytes to the left of global variable 'mvhd' defined in '../../frontend/mp4read.c:802:22' (0x56118d728260) of size 32
0x56118d728230 is located 0 bytes to the right of global variable 'trak' defined in '../../frontend/mp4read.c:806:22' (0x56118d728020) of size 528
SUMMARY: AddressSanitizer: global-buffer-overflow ../../frontend/mp4read.c:746 in parse
Shadow bytes around the buggy address:
  0x0ac2b1adcff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add000: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add030: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ac2b1add040: 00 00 00 00 00 00[f9]f9 f9 f9 f9 f9 00 00 00 00
  0x0ac2b1add050: f9 f9 f9 f9 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add060: 00 00 00 00 f9 f9 f9 f9 00 00 00 00 00 00 00 00
  0x0ac2b1add070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac2b1add080: f9 f9 f9 f9 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9
  0x0ac2b1add090: 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9 00 00 00 00
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
==73817==ABORTING

2. There was a heap-buffer-overflow bug in function excluded_channels() in libfaad/syntax.c:2297.

fish@ubuntu:~ ./afl/afl/bin/faad  -o outfile.wav  heap-buffer-overflow-2
 *********** Ahead Software MPEG-4 AAC Decoder V2.8.8 ******************

 Build: Nov 11 2018
 Copyright 2002-2004: Ahead Software AG
 http://www.audiocoding.com
 bug tracking: https://sourceforge.net/p/faac/bugs/
 Floating point version

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License.

 **************************************************************************

faad000_id_000000,sig_06,src_000000,op_havoc,rep_128 file info:
RAW

=================================================================
==77978==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x610000000100 at pc 0x7ff1d5923ab5 bp 0x7ffc701f4560 sp 0x7ffc701f4550
WRITE of size 1 at 0x610000000100 thread T0
    #0 0x7ff1d5923ab4 in excluded_channels ../../libfaad/syntax.c:2297
    #1 0x7ff1d5923ab4 in dynamic_range_info ../../libfaad/syntax.c:2236
    #2 0x7ff1d5923ab4 in extension_payload ../../libfaad/syntax.c:2166
    #3 0x7ff1d5923ab4 in fill_element ../../libfaad/syntax.c:1110
    #4 0x7ff1d5941b89 in raw_data_block ../../libfaad/syntax.c:500
    #5 0x7ff1d58a4f0a in aac_frame_decode ../../libfaad/decoder.c:990
    #6 0x559b61ee4f99 in decodeAACfile ../../frontend/main.c:679
    #7 0x559b61ee4f99 in faad_main ../../frontend/main.c:1323
    #8 0x7ff1d54b3b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #9 0x559b61ecae69 in _start (/home/fish/Desktop/2018-10-10/sound_audio/faad2/afl/afl/bin/faad+0xae69)

0x610000000100 is located 0 bytes to the right of 192-byte region [0x610000000040,0x610000000100)
allocated by thread T0 here:
    #0 0x7ff1d5ce6b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x7ff1d58b18b1 in drc_init ../../libfaad/drc.c:41

SUMMARY: AddressSanitizer: heap-buffer-overflow ../../libfaad/syntax.c:2297 in excluded_channels
Shadow bytes around the buggy address:
  0x0c207fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c207fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c207fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c207fff8000: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c207fff8010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c207fff8020:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c207fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c207fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c207fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c207fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c207fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==77978==ABORTING

3. 

There was a stack-buffer-overflow bug in function calculate_gain() in libfaad/sbr_hfadj.c:1346.

fish@ubuntu:./afl/afl/bin/faad  -o outfile.wav  stack-buffer-overflow-3 
 *********** Ahead Software MPEG-4 AAC Decoder V2.8.8 ******************

 Build: Nov 11 2018
 Copyright 2002-2004: Ahead Software AG
 http://www.audiocoding.com
 bug tracking: https://sourceforge.net/p/faac/bugs/
 Floating point version

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License.

 **************************************************************************

01POC file info:
ADTS, 12.416 sec, 37 kbps, 48000 Hz

  ---------------------
 | Config:  2 Ch       |
  ---------------------
 | Ch |    Position    |
  ---------------------
 | 00 | Left front     |
 | 01 | Right front    |
  ---------------------

=================================================================
==79181==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffc6aed724c at pc 0x7f103eda0947 bp 0x7ffc6aed62b0 sp 0x7ffc6aed62a0
WRITE of size 4 at 0x7ffc6aed724c thread T0
    #0 0x7f103eda0946 in calculate_gain ../../libfaad/sbr_hfadj.c:1346
    #1 0x7f103eda0946 in hf_adjustment ../../libfaad/sbr_hfadj.c:83
    #2 0x7f103eddc1a1 in sbr_process_channel ../../libfaad/sbr_dec.c:363
    #3 0x7f103eddc1a1 in sbrDecodeSingleFramePS ../../libfaad/sbr_dec.c:637
    #4 0x7f103ed0f26d in reconstruct_single_channel ../../libfaad/specrec.c:1071
    #5 0x7f103ed3639b in single_lfe_channel_element ../../libfaad/syntax.c:631
    #6 0x7f103ed44ba8 in decode_sce_lfe ../../libfaad/syntax.c:351
    #7 0x7f103ed44ba8 in raw_data_block ../../libfaad/syntax.c:441
    #8 0x7f103eca4f0a in aac_frame_decode ../../libfaad/decoder.c:990
    #9 0x561ad7895f99 in decodeAACfile ../../frontend/main.c:679
    #10 0x561ad7895f99 in faad_main ../../frontend/main.c:1323
    #11 0x7f103e8b3b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #12 0x561ad787be69 in _start (/home/fish/Desktop/2018-10-10/sound_audio/faad2/afl/afl/bin/faad+0xae69)

Address 0x7ffc6aed724c is located in stack of thread T0 at offset 3740 in frame
    #0 0x7f103ed9a21f in hf_adjustment ../../libfaad/sbr_hfadj.c:60

  This frame has 4 object(s):
    [32, 228) 'Q_M_lim'
    [288, 484) 'G_lim'
    [544, 740) 'S_M'
    [800, 3740) 'adj' <== Memory access at offset 3740 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow ../../libfaad/sbr_hfadj.c:1346 in calculate_gain
Shadow bytes around the buggy address:
  0x10000d5d2df0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10000d5d2e40: 00 00 00 00 00 00 00 00 00[04]f3 f3 f3 f3 00 00
  0x10000d5d2e50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e70: 00 00 f1 f1 f1 f1 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10000d5d2e90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==79181==ABORTING

4. There is an out-of-bound read bug in ifilter_bank() in libfaad/filtbank.c:307.

fish@ubuntu:./afl/afl/bin/faad  -o outfile.wav  out-of-bound-read-4
 *********** Ahead Software MPEG-4 AAC Decoder V2.8.8 ******************

 Build: Nov 11 2018
 Copyright 2002-2004: Ahead Software AG
 http://www.audiocoding.com
 bug tracking: https://sourceforge.net/p/faac/bugs/
 Floating point version

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License.

 **************************************************************************

02POC file info:
ADTS, 12.416 sec, 37 kbps, 48000 Hz

  ---------------------
 | Config:  2 Ch       |
  ---------------------
 | Ch |    Position    |
  ---------------------
 | 00 | Left front     |
 | 01 | Right front    |
  ---------------------

ASAN:DEADLYSIGNAL.
=================================================================
==80424==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f5beda94d2f bp 0x000000000000 sp 0x7fffd63e1830 T0)
==80424==The signal is caused by a READ memory access.
==80424==Hint: address points to the zero page.
    #0 0x7f5beda94d2e in ifilter_bank ../../libfaad/filtbank.c:307
    #1 0x7f5bedaf05d1 in reconstruct_channel_pair ../../libfaad/specrec.c:1258
    #2 0x7f5bedb15760 in channel_pair_element ../../libfaad/syntax.c:759
    #3 0x7f5bedb22260 in decode_cpe ../../libfaad/syntax.c:402
    #4 0x7f5bedb22260 in raw_data_block ../../libfaad/syntax.c:448
    #5 0x7f5beda82f0a in aac_frame_decode ../../libfaad/decoder.c:990
    #6 0x563aa00f0f99 in decodeAACfile ../../frontend/main.c:679
    #7 0x563aa00f0f99 in faad_main ../../frontend/main.c:1323
    #8 0x7f5bed691b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #9 0x563aa00d6e69 in _start (/home/fish/Desktop/2018-10-10/sound_audio/faad2/afl/afl/bin/faad+0xae69)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV ../../libfaad/filtbank.c:307 in ifilter_bank
==80424==ABORTING


```
