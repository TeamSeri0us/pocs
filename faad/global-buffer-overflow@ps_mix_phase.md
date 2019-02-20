## Description

FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.

## Version

[2.8.8](https://sourceforge.net/projects/faac/files/faad2-src/faad2-2.8.0/)

## Others

this bug is reported by pwd@360TeamSeri0us, 
please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details

    ./faad global-buffer-overflow@ps_mix_phase

## src

  underflow in ps_dec.c

```c
In file: /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/ps_dec.c
   1507                 */
   1508 
   1509                 //printf("%d\n", ps->iid_index[env][bk]);
   1510 
   1511                 /* calculate the scalefactors c_1 and c_2 from the intensity differences */
 ► 1512                 c_1 = sf_iid[no_iid_steps + ps->iid_index[env][bk]];
   1513                 c_2 = sf_iid[no_iid_steps - ps->iid_index[env][bk]];
   1514 
   1515                 /* calculate alpha and beta using the ICC parameters */
   1516                 cosa = cos_alphas[ps->icc_index[env][bk]];
   1517                 sina = sin_alphas[ps->icc_index[env][bk]];
// p no_iid_steps
// $5 = -9 '\367'
// pwndbg> p sf_iid[no_iid_steps + ps->iid_index[env][bk]]
// $6 = 0.0031573684
// pwndbg> p no_iid_steps 
// $7 = 7 '\a'
// pwndbg> p no_iid_steps + ps->iid_index[env][bk]
// $8 = -2

```

## patch

  chech the index of sf_iid is in [0, 14]

## asan report

```txt
=================================================================
==3376==ERROR: AddressSanitizer: global-buffer-overflow on address 0x7ffff7bb7238 at pc 0x7ffff7b0e4ce bp 0x7ffffffe5a10 sp 0x7ffffffe5a08
READ of size 4 at 0x7ffff7bb7238 thread T0
[New process 3386]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
process 3386 is executing new program: /home/pwd/llvm_dev/llvm-install/bin/llvm-symbolizer
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    #0 0x7ffff7b0e4cd in ps_mix_phase /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/ps_dec.c:1512:23
    #1 0x7ffff7b0e4cd in ps_decode /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/ps_dec.c:2000
    #2 0x7ffff7ba7fa8 in sbrDecodeSingleFramePS /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/sbr_dec.c:657:9
    #3 0x7ffff7b1e401 in reconstruct_single_channel /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/specrec.c:1071:22
    #4 0x7ffff7b2c66b in single_lfe_channel_element /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/syntax.c:631:14
    #5 0x7ffff7b2c66b in decode_sce_lfe /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/syntax.c:351
    #6 0x7ffff7b2a781 in raw_data_block /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/syntax.c:441:17
    #7 0x7ffff7ad032d in aac_frame_decode /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/decoder.c:990:9
    #8 0x524c00 in decodeAACfile /home/pwd/fuzz/fuzz-faad2/faad2/frontend/main.c:679:25
    #9 0x524c00 in faad_main /home/pwd/fuzz/fuzz-faad2/faad2/frontend/main.c:1323
    #10 0x524c00 in main /home/pwd/fuzz/fuzz-faad2/faad2/frontend/main.c:1366
    #11 0x7ffff6b06b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #12 0x41a769 in _start (/home/pwd/fuzz/fuzz-faad2/faad2/installed-asan/bin/faad+0x41a769)

0x7ffff7bb7238 is located 8 bytes to the left of global variable 'sf_iid_normal' defined in './ps_tables.h:524:21' (0x7ffff7bb7240) of size 60
0x7ffff7bb7238 is located 28 bytes to the right of global variable 'sf_iid_fine' defined in './ps_tables.h:532:21' (0x7ffff7bb71a0) of size 124
SUMMARY: AddressSanitizer: global-buffer-overflow /home/pwd/fuzz/fuzz-faad2/faad2/libfaad/ps_dec.c:1512:23 in ps_mix_phase
Shadow bytes around the buggy address:
  0x10007ef6edf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007ef6ee00: 00 00 00 00 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x10007ef6ee10: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x10007ef6ee20: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x10007ef6ee30: f9 f9 f9 f9 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10007ef6ee40: 00 00 00 04 f9 f9 f9[f9]00 00 00 00 00 00 00 04
  0x10007ef6ee50: f9 f9 f9 f9 00 00 00 00 f9 f9 f9 f9 00 00 00 00
  0x10007ef6ee60: f9 f9 f9 f9 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007ef6ee70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007ef6ee80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007ef6ee90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==3376==ABORTING
[Inferior 2 (process 3386) exited normally]
```