

## description

This package provides encoder/decoder implementation for DEC SIXEL graphics, and some converter programs.

## version

v1.8.2

## others

this bug is reported by fish@360TeamSeri0us, please send email to teamSeri0us360@gmail.com if you have any question.

## Details

`./sixel2png infinite_loop_poc1`

```
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ source:../../src/fromsixel.c+561 ]────
    556	             default:
    557	                 if (*p >= '?' && *p <= '~') {  /* sixel characters */
    558	                     if (image->width < (context->pos_x + context->repeat_count) || image->height < (context->pos_y + 6)) {
    559	                         sx = image->width * 2;
    560	                         sy = image->height * 2;
		// context=0x00007fffffffd6a0  →  [...]  →  0x0000000000000003, sx=0x0, sy=-0x80000000
 →  561	                         while (sx < (context->pos_x + context->repeat_count) || sy < (context->pos_y + 6)) {
    562	                             sx *= 2;
    563	                             sy *= 2;
    564	                         }
    565	                         status = image_buffer_resize(image, sx, sy, context->bgindex, allocator);
    566	                         if (SIXEL_FAILED(status)) {
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "sixel2png", stopped, reason: SINGLE STEP
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7b7ed89 → Name: sixel_decode_raw_impl(p=0x555555774630 "^\033\\", len=0x53, image=0x7fffffffd7e0, context=0x7fffffffd760, allocator=0x555555774300)
[#1] 0x7ffff7b7f8b3 → Name: sixel_decode_raw(p=0x5555557745e0 "\033Pq\"1;1;70;11#1;2;", '1' <repeats 13 times>, "9;19;19#0!70~-!7", '1' <repeats 25 times>, "\"1111110^\033\\", len=0x53, pixels=0x7fffffffdc58, pwidth=0x7fffffffdc3c, pheight=0x7fffffffdc40, palette=0x7fffffffdc60, ncolors=0x7fffffffdc44, allocator=0x555555774300)
[#2] 0x7ffff7bacc8c → Name: sixel_decoder_decode(decoder=0x555555774330)
[#3] 0x555555554ea6 → Name: main(argc=0x2, argv=0x7fffffffde68)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
561	                        while (sx < (context->pos_x + context->repeat_count) || sy < (context->pos_y + 6)) {
1: sx = 0x0
gef➤  p context->pos_x + context->repeat_count
$32 = 0x471c71c7

```


`./img2sixel heap-buffer-overflow-poc2 `


```
Corrupt JPEG data: premature end of data segment
=================================================================
==100553==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7fc919e46f94 at pc 0x7fca3cf50228 bp 0x7fffe7f5e600 sp 0x7fffe7f5e5f8
READ of size 1 at 0x7fc919e46f94 thread T0
==100553==WARNING: failed to fork (errno 12)
==100553==WARNING: failed to fork (errno 12)
==100553==WARNING: failed to fork (errno 12)
==100553==WARNING: failed to fork (errno 12)
==100553==WARNING: failed to fork (errno 12)
==100553==WARNING: Failed to use and restart external symbolizer!
    #0 0x7fca3cf50227  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x70227)
    #1 0x7fca3cf4c758  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x6c758)
    #2 0x7fca3cf53ae5  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x73ae5)
    #3 0x7fca3cf36b25  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x56b25)
    #4 0x7fca3d028e26  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x148e26)
    #5 0x7fca3cf88581  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0xa8581)
    #6 0x7fca3d0264de  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x1464de)
    #7 0x50564a  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/bin/img2sixel+0x50564a)
    #8 0x7fca3bf2fb96  (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #9 0x41c139  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/bin/img2sixel+0x41c139)

0x7fc919e46f94 is located 0 bytes to the right of 433805204-byte region [0x7fc900091800,0x7fc919e46f94)
allocated by thread T0 here:
    #0 0x4cb710  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/bin/img2sixel+0x4cb710)
    #1 0x7fca3d028ba1  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x148ba1)
    #2 0x7fca3cf88581  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0xa8581)
    #3 0x7fca3d0264de  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x1464de)
    #4 0x50564a  (/home/fish/Desktop/dumb/image/libsixel/fast/fast/bin/img2sixel+0x50564a)
    #5 0x7fca3bf2fb96  (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow (/home/fish/Desktop/dumb/image/libsixel/fast/fast/lib/libsixel.so.1+0x70227) 
Shadow bytes around the buggy address:
  0x0ff9a33c0da0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff9a33c0db0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff9a33c0dc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff9a33c0dd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff9a33c0de0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ff9a33c0df0: 00 00[04]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff9a33c0e00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff9a33c0e10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff9a33c0e20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff9a33c0e30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff9a33c0e40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==100553==ABORTING


gef➤  bt
#0  __memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:249
#1  0x00007ffff7ba4bae in load_jpeg (result=0x555555777428, data=0x7ffff7fd4010 "\377\330\377", <incomplete sequence \340>, datasize=0x1263b, pwidth=0x555555777438, pheight=0x55555577743c, ppixelformat=0x555555777444, allocator=0x555555777300) at ../../src/loader.c:198
#2  0x00007ffff7ba62d7 in load_with_builtin (pchunk=0x5555557773f0, fstatic=0x0, fuse_palette=0x1, reqcolors=0x100, bgcolor=0x0, loop_control=0x0, fn_load=0x7ffff7bac395 <load_image_callback>, context=0x555555777330) at ../../src/loader.c:820
#3  0x00007ffff7ba67d1 in sixel_helper_load_image_file (filename=0x7fffffffe247 "/home/fish/testcase/images/jpg/random.jpg", fstatic=0x0, fuse_palette=0x1, reqcolors=0x100, bgcolor=0x0, loop_control=0x0, fn_load=0x7ffff7bac395 <load_image_callback>, finsecure=0x0, cancel_flag=0x555555759014 <signaled>, context=0x555555777330, allocator=0x555555777300) at ../../src/loader.c:1352
#4  0x00007ffff7bac50e in sixel_encoder_encode (encoder=0x555555777330, filename=0x7fffffffe247 "/home/fish/testcase/images/jpg/random.jpg") at ../../src/encoder.c:1737
#5  0x0000555555555545 in main (argc=0x2, argv=0x7fffffffde78) at ../../converters/img2sixel.c:457

```


