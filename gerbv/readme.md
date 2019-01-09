

## target 

* Gerbv is an open source Gerber file (RS-274X only) viewer. Gerbv lets you load several files on top of each other, do measurements on the displayed image, etc. Besides viewing Gerbers, you may also view Excellon drill files as well as pick-place file.

## version

 [2.7rc0](https://sourceforge.net/projects/gerbv/files/gerbv/gerbv-2.7/gerbv-2.7rc0.tar.gz/download)

## others

This bug is reported by fish@360TeamSeri0us, please send email to teamSeri0us360@gmail.com if you have any question.

## details 


`1. There is a  heap-buffer-overflow problem in function simplify_aperture_macro() in src/gerber.c:`


###  stack backtrace
```
 fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ ./fast/fast/bin/gerbv --export=png -o out.png heap-bof-poc-1

** (process:12477): CRITICAL **: 23:25:37.524: Number of parameters to aperture macro (685) are more than gerbv is able to store (102)
=================================================================
==12477==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60e00000dba0 at pc 0x0000004c1c21 bp 0x7ffe805393d0 sp 0x7ffe80538b80
READ of size 816 at 0x60e00000dba0 thread T0
    #0 0x4c1c20 in __asan_memcpy (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x4c1c20)
    #1 0x7f05a250dc49 in simplify_aperture_macro /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:2049:3
    #2 0x7f05a250dc49 in parse_aperture_definition /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:2270
    #3 0x7f05a250dc49 in parse_rs274x /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:1635
    #4 0x7f05a250dc49 in gerber_parse_file_segment /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:243
    #5 0x7f05a2519564 in parse_gerb /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:768:16
    #6 0x7f05a251c746 in gerbv_open_image /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:526:18
    #7 0x7f05a251d2dd in gerbv_open_layer_from_filename_with_color /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:249:7
    #8 0x54f196 in main /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/main.c:1005:3
    #9 0x7f059f025b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #10 0x427e29 in _start (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x427e29)

0x60e00000dba0 is located 0 bytes to the right of 160-byte region [0x60e00000db00,0x60e00000dba0)
allocated by thread T0 here:
    #0 0x4d7608 in calloc (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x4d7608)
    #1 0x7f05a029ba80 in g_malloc0 (/usr/lib/x86_64-linux-gnu/libglib-2.0.so.0+0x51a80)
    #2 0x7f05a2519564 in parse_gerb /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:768:16

SUMMARY: AddressSanitizer: heap-buffer-overflow (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x4c1c20) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c1c7fff9b20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c1c7fff9b30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c1c7fff9b40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c1c7fff9b50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c1c7fff9b60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c1c7fff9b70: 00 00 00 00[fa]fa fa fa fa fa fa fa 00 00 00 00
  0x0c1c7fff9b80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 fa
  0x0c1c7fff9b90: fa fa fa fa fa fa fa fa fd fd fd fd fd fd fd fd
  0x0c1c7fff9ba0: fd fd fd fd fd fd fd fd fd fd fd fd fa fa fa fa
  0x0c1c7fff9bb0: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c1c7fff9bc0: fd fd fd fd fd fd fd fa fa fa fa fa fa fa fa fa
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
==12477==ABORTING

```

### src 

```
	/*
		 * Create struct for simplified aperture macro and
		 * start filling in the blanks.
		 */
		sam = g_new (gerbv_simplified_amacro_t, 1);
		sam->type = type;
		sam->next = NULL;
		memset(sam->parameter, 0, 
		       sizeof(double) * APERTURE_PARAMETERS_MAX);
		memcpy(sam->parameter, s->stack,        //   out-of-bound read 816 bytes
		       sizeof(double) *  nuf_parameters); 

```



`2. There is a  heap-buffer-overflow problem in function simplify_aperture_macro() in src/gerber.c:`


### stack backtrace 
```
fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ ./fast/fast/bin/gerbv --export=png -o out.png heap-bof-poc-2
=================================================================
==12479==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61800000e878 at pc 0x7f5f574460a6 bp 0x7ffe5efb1910 sp 0x7ffe5efb1908
READ of size 8 at 0x61800000e878 thread T0
    #0 0x7f5f574460a5 in simplify_aperture_macro /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:1937:14
    #1 0x7f5f574460a5 in parse_aperture_definition /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:2270
    #2 0x7f5f574460a5 in parse_rs274x /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:1635
    #3 0x7f5f574460a5 in gerber_parse_file_segment /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:243
    #4 0x7f5f57447564 in parse_gerb /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:768:16
    #5 0x7f5f5744a746 in gerbv_open_image /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:526:18
    #6 0x7f5f5744b2dd in gerbv_open_layer_from_filename_with_color /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:249:7
    #7 0x54f196 in main /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/main.c:1005:3
    #8 0x7f5f53f53b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #9 0x427e29 in _start (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x427e29)

0x61800000e878 is located 8 bytes to the left of 816-byte region [0x61800000e880,0x61800000ebb0)
allocated by thread T0 here:
    #0 0x4d7400 in __interceptor_malloc (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x4d7400)
    #1 0x7f5f551c9a28 in g_malloc (/usr/lib/x86_64-linux-gnu/libglib-2.0.so.0+0x51a28)
    #2 0x7f5f57447564 in parse_gerb /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:768:16

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:1937:14 in simplify_aperture_macro
Shadow bytes around the buggy address:
  0x0c307fff9cb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c307fff9cc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c307fff9cd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c307fff9ce0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c307fff9cf0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c307fff9d00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]
  0x0c307fff9d10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c307fff9d20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c307fff9d30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c307fff9d40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c307fff9d50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==12479==ABORTING
```

### src
```
/* Make a copy of the parameter list that we can rewrite if necessary */
    lp = g_new (double,APERTURE_PARAMETERS_MAX);

    memcpy(lp, aperture->parameter, sizeof(double) * APERTURE_PARAMETERS_MAX);
    
    for(ip = aperture->amacro->program; ip != NULL; ip = ip->next) {
	switch(ip->opcode) {
	case GERBV_OPCODE_NOP:
	    break;
	case GERBV_OPCODE_PUSH :
	    push(s, ip->data.fval);
	    break;
        case GERBV_OPCODE_PPUSH :
	    push(s, lp[ip->data.ival - 1]);   // out-of-bound read 8 bytes
	    break;
	case GERBV_OPCODE_PPOP:
	    if (pop(s, &tmp[0]) < 0)
		GERB_FATAL_ERROR(_("Tried to pop an empty stack"));
	    lp[ip->data.ival - 1] = tmp[0];
	    break;

```


`3. There is a null-pointer-dereference problem in function parse_aperture_definition() in file src/gerber.c:`

### stack backtrace
```
fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ ./fast/fast/bin/gerbv --export=png -o out.png null-pointer-dereference-poc-3 


** (process:113681): CRITICAL **: 20:50:09.412: Found unknown character '\xfe' (0xfffffffe) at line 1 in file "/home/fish/Desktop/dumb/image/gerbv-2.7rc0/null-pointer-dereference-poc-3"
......
** (process:113681): CRITICAL **: 20:50:09.445: Unknown RS-274X extension found %\n%% at line 20 in file ""/home/fish/Desktop/dumb/image/gerbv-2.7rc0/null-pointer-dereference-poc-3"


ASAN:DEADLYSIGNAL
=================================================================
==12965==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fae8dd3eb72 bp 0x7fae8e08da68 sp 0x7ffe52edab60 T0)
==12965==The signal is caused by a READ memory access.
==12965==Hint: address points to the zero page.
    #0 0x7fae8dd3eb71 in strtok_r /build/glibc-OTsEL5/glibc-2.27/string/strtok_r.c:46
    #1 0x7fae911a3967 in parse_aperture_definition /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:2189:13
    #2 0x7fae911a3967 in parse_rs274x /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:1635
    #3 0x7fae911a3967 in gerber_parse_file_segment /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:243
    #4 0x7fae911b5564 in parse_gerb /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerber.c:768:16
    #5 0x7fae911b8746 in gerbv_open_image /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:526:18
    #6 0x7fae911b92dd in gerbv_open_layer_from_filename_with_color /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/gerbv.c:249:7
    #7 0x54f196 in main /home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/src/../../src/main.c:1005:3
    #8 0x7fae8dcc1b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #9 0x427e29 in _start (/home/fish/Desktop/dumb/image/gerbv-2.7rc0/fast/fast/bin/gerbv+0x427e29)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /build/glibc-OTsEL5/glibc-2.27/string/strtok_r.c:46 in strtok_r
==12965==ABORTING


```

### src

```
 /*
     * Read in the whole aperture defintion and tokenize it
     */
    ad = gerb_fgetstring(fd, '*');
    token = strtok(ad, ",");      // the address of ad is 0x0,can't access.
    
    if (token == NULL) {
	gerbv_stats_printf(error_list, GERBV_MESSAGE_ERROR, -1,
		_("Invalid aperture definition "
		    "at line %ld in file \"%s\""),
		*line_num_p, fd->filename);
	return -1;
    }


```



`4. There is an assertion in function _cairo_arc_in_direction in file  cairo-arc.c:189.`

fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ ./debug/debug/bin/gerbv --export=png -o out.png cairo-abort-poc-4
gerbv: cairo-arc.c:189: _cairo_arc_in_direction: Assertion `angle_max >= angle_min' failed.
Aborted (core dumped)


### stack backtrace
```
gef➤  bt
#0  0x00007ffff58e4e97 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff58e6801 in __GI_abort () at abort.c:79
#2  0x00007ffff58d639a in __assert_fail_base (fmt=0x7ffff5a5d7d8 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x7ffff5f97a3c "angle_max >= angle_min", file=file@entry=0x7ffff5f97a30 "cairo-arc.c", line=line@entry=0xbd, function=function@entry=0x7ffff5f97a60 <__PRETTY_FUNCTION__.12709> "_cairo_arc_in_direction") at assert.c:92
#3  0x00007ffff58d6412 in __GI___assert_fail (assertion=assertion@entry=0x7ffff5f97a3c "angle_max >= angle_min", file=file@entry=0x7ffff5f97a30 "cairo-arc.c", line=line@entry=0xbd, function=function@entry=0x7ffff5f97a60 <__PRETTY_FUNCTION__.12709> "_cairo_arc_in_direction") at assert.c:101
#4  0x00007ffff5eca355 in _cairo_arc_in_direction (cr=0x5555557be4d0, xc=0, yc=0, radius=0.0078740158653634752, angle_min=nan(0x8000000000000), angle_max=nan(0x8000000000000), dir=CAIRO_DIRECTION_FORWARD) at cairo-arc.c:189
#5  0x00007ffff5ededd5 in _cairo_default_context_arc (abstract_cr=0x5555557be4d0, xc=<optimized out>, yc=<optimized out>, radius=<optimized out>, angle1=nan(0x8000000000000), angle2=nan(0x8000000000000), forward=0x1) at cairo-default-context.c:783
#6  0x00007ffff5f3d6eb in cairo_arc (cr=0x5555557be4d0, xc=<optimized out>, yc=<optimized out>, radius=<optimized out>, angle1=<optimized out>, angle2=<optimized out>) at cairo.c:1860
#7  0x00007ffff7bac76c in gerbv_draw_amacro (cairoTarget=0x5555557be4d0, clearOperator=CAIRO_OPERATOR_CLEAR, darkOperator=CAIRO_OPERATOR_OVER, s=0x5555557d41c0, usesClearPrimitive=0x0, pixelWidth=0.013888888888888888, drawMode=DRAW_IMAGE, selectionInfo=0x0, image=0x5555557bf370, net=0x5555557d55f0) at ../../src/draw.c:616
#8  0x00007ffff7baf3c6 in draw_image_to_cairo_target (cairoTarget=0x5555557be4d0, image=0x5555557bf370, pixelWidth=0.013888888888888888, drawMode=DRAW_IMAGE, selectionInfo=0x0, renderInfo=0x7fffffffdc70, allowOptimization=0x1, transform=..., pixelOutput=0x1) at ../../src/draw.c:1420
#9  0x00007ffff7bc7420 in gerbv_render_layer_to_cairo_target_without_transforming (cr=0x5555557be4d0, fileInfo=0x5555557be2c0, renderInfo=0x7fffffffdc70, pixelOutput=0x1) at ../../src/gerbv.c:997
#10 0x00007ffff7bc71c5 in gerbv_render_layer_to_cairo_target (cr=0x5555557be4d0, fileInfo=0x5555557be2c0, renderInfo=0x7fffffffdc70) at ../../src/gerbv.c:956
#11 0x00007ffff7bc712d in gerbv_render_all_layers_to_cairo_target (gerbvProject=0x5555557bbbc0, cr=0x5555557be4d0, renderInfo=0x7fffffffdc70) at ../../src/gerbv.c:942
#12 0x00007ffff7bb5a87 in gerbv_export_png_file_from_project (gerbvProject=0x5555557bbbc0, renderInfo=0x7fffffffdc70, filename=0x7fffffffe22e "out.png") at ../../src/export-image.c:87
#13 0x000055555558208e in main (argc=0x5, argv=0x7fffffffde28) at ../../src/main.c:1123

gef➤  p startAngle1
$1 = nan(0x8000000000000)
gef➤  p endAngle1
$2 = nan(0x8000000000000)

```

### src
```

    186	     if (cairo_status (cr))
    187	         return;
    188	 
 →  189	     assert (angle_max >= angle_min);  // assert failed.
    190	 
    191	     if (angle_max - angle_min > 2 * M_PI * MAX_FULL_CIRCLES) {
    192	 	angle_max = fmod (angle_max - angle_min, 2 * M_PI);
    193	 	angle_min = fmod (angle_min, 2 * M_PI);
    194	 	angle_max += angle_min + 2 * M_PI * MAX_FULL_CIRCLES;

```



`5. There is an assertion problem in libglib-2.0.`

fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ ./debug/debug/bin/gerbv   ./debug/debug/bin/gerbv glib-abort-poc-5
Gtk-Message: 22:42:14.336: Failed to load module "canberra-gtk-module"
(process:6546): Gtk-CRITICAL (recursed) **: gtk_text_buffer_emit_insert: assertion 'g_utf8_validate (text, len, NULL)' failedAborted (core dumped)

### stack backtrace 

```
0x00007ffff6229e11 in ?? () from /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
gef➤  bt
#0  0x00007ffff6229e11 in  () at /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
#1  0x00007ffff622aeac in g_log_default_handler () at /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff622b13d in g_logv () at /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x00007ffff622b2af in g_log () at /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
#4  0x00007ffff6229b09 in g_realloc () at /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
#5  0x00007ffff7ba8f4e in draw_gdk_render_polygon_object (oldNet=0x5555557d83d0, image=0x5555557bf3f0, sr_x=0, sr_y=0, fullMatrix=0x7fffffffac00, scaleMatrix=0x7fffffffac30, gc=0x555555a98130, pgc=0x555555a981d0, pixmap=0x7fffffffadb0) at ../../src/draw-gdk.c:783
#6  0x00007ffff7ba9fed in draw_gdk_image_to_pixmap (pixmap=0x7fffffffadb0, image=0x5555557bf3f0, scale=1127.6190476190475, trans_x=246.71428571428581, trans_y=577.90476190476193, drawMode=DRAW_IMAGE, selectionInfo=0x0, renderInfo=0x5555557a9980 <screenRenderInfo>, transform=...) at ../../src/draw-gdk.c:1060
#7  0x00007ffff7bc6ab6 in gerbv_render_to_pixmap_using_gdk (gerbvProject=0x5555557bbbc0, pixmap=0x5555559960c0, renderInfo=0x5555557a9980 <screenRenderInfo>, selectionInfo=0x5555557a98b8 <screen+888>, selectionColor=0x5555557a9568 <screen+40>) at ../../src/gerbv.c:821
#8  0x0000555555586d9d in render_refresh_rendered_image_on_screen () at ../../src/render.c:441
#9  0x000055555556f6be in callbacks_drawingarea_configure_event (widget=0x5555559795e0, event=0x5555559b6f40) at ../../src/callbacks.c:3236
#10 0x00007ffff70ec38b in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#11 0x00007ffff64fe10d in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#12 0x00007ffff651105e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#13 0x00007ffff65190af in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#14 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#15 0x00007ffff72022bc in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#16 0x00007ffff707489a in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#17 0x00007ffff70748e9 in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#18 0x00007ffff64fe10d in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#19 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#20 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#21 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#22 0x00007ffff72083d8 in gtk_widget_realize () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#23 0x00007ffff72085f8 in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#24 0x00007ffff71712f8 in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#25 0x00007ffff70712ff in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#26 0x00007ffff64fe021 in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#27 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#28 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#29 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#30 0x00007ffff72085ce in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#31 0x00007ffff703dc85 in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#32 0x00007ffff70712ff in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#33 0x00007ffff64fe021 in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#34 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#35 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#36 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#37 0x00007ffff72085ce in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#38 0x00007ffff70712ff in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#39 0x00007ffff64fe021 in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#40 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#41 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#42 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#43 0x00007ffff72085ce in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#44 0x00007ffff703dc85 in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#45 0x00007ffff70712ff in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#46 0x00007ffff64fe021 in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#47 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#48 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#49 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#50 0x00007ffff72085ce in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#51 0x00007ffff7218cea in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#52 0x00007ffff64fe10d in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#53 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#54 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#55 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#56 0x00007ffff72085ce in gtk_widget_map () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#57 0x00007ffff72129d9 in  () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#58 0x00007ffff64fe10d in g_closure_invoke () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#59 0x00007ffff651112e in  () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#60 0x00007ffff6519715 in g_signal_emit_valist () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#61 0x00007ffff651a12f in g_signal_emit () at /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#62 0x00007ffff7207b96 in gtk_widget_show () at /usr/lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
#63 0x000055555557c328 in interface_create_gui (req_width=0xffffffff, req_height=0xffffffff) at ../../src/interface.c:1753
#64 0x0000555555582350 in main (argc=0x2, argv=0x7fffffffde28) at ../../src/main.c:1185

```




`6. There is an infinite-loop in function _arc_error_normalized (double angle) in file cairo-arc.c.`

fish@ubuntu:~/Desktop/dumb/image/gerbv-2.7rc0$ gdb -q --args ./debug/debug/bin/gerbv --export=png -o out.png hangs-poc-6

### stack backtrace 
```
gef➤  bt
#0  0x00007ffff5ec9f97 in _arc_max_angle_for_tolerance_normalized (tolerance=0) at cairo-arc.c:101
#1  0x00007ffff5ec9f97 in _arc_segments_needed (tolerance=<optimized out>, ctm=0x7fffffffd4f0, radius=inf, angle=<optimized out>) at cairo-arc.c:119
#2  0x00007ffff5ec9f97 in _cairo_arc_in_direction (cr=0x5555557be290, xc=0, yc=0, radius=inf, angle_min=<optimized out>, angle_max=<optimized out>, dir=CAIRO_DIRECTION_FORWARD) at cairo-arc.c:223
#3  0x00007ffff5ededd5 in _cairo_default_context_arc (abstract_cr=0x5555557be290, xc=<optimized out>, yc=<optimized out>, radius=<optimized out>, angle1=0, angle2=1.5707963267948966, forward=0x1) at cairo-default-context.c:783
#4  0x00007ffff5f3d6eb in cairo_arc (cr=0x5555557be290, xc=<optimized out>, yc=<optimized out>, radius=<optimized out>, angle1=<optimized out>, angle2=<optimized out>) at cairo.c:1860
#5  0x00007ffff7bac76c in gerbv_draw_amacro (cairoTarget=0x5555557be290, clearOperator=CAIRO_OPERATOR_CLEAR, darkOperator=CAIRO_OPERATOR_OVER, s=0x5555557d49d0, usesClearPrimitive=0x0, pixelWidth=0.013888888888888888, drawMode=DRAW_IMAGE, selectionInfo=0x0, image=0x5555557bf3e0, net=0x5555557d5740) at ../../src/draw.c:616
#6  0x00007ffff7baf3c6 in draw_image_to_cairo_target (cairoTarget=0x5555557be290, image=0x5555557bf3e0, pixelWidth=0.013888888888888888, drawMode=DRAW_IMAGE, selectionInfo=0x0, renderInfo=0x7fffffffdbd0, allowOptimization=0x1, transform=..., pixelOutput=0x1) at ../../src/draw.c:1420
#7  0x00007ffff7bc7420 in gerbv_render_layer_to_cairo_target_without_transforming (cr=0x5555557be290, fileInfo=0x5555557be210, renderInfo=0x7fffffffdbd0, pixelOutput=0x1) at ../../src/gerbv.c:997
#8  0x00007ffff7bc71c5 in gerbv_render_layer_to_cairo_target (cr=0x5555557be290, fileInfo=0x5555557be210, renderInfo=0x7fffffffdbd0) at ../../src/gerbv.c:956
#9  0x00007ffff7bc712d in gerbv_render_all_layers_to_cairo_target (gerbvProject=0x5555557bbbc0, cr=0x5555557be290, renderInfo=0x7fffffffdbd0) at ../../src/gerbv.c:942
#10 0x00007ffff7bb5a87 in gerbv_export_png_file_from_project (gerbvProject=0x5555557bbbc0, renderInfo=0x7fffffffdbd0, filename=0x7fffffffe1a0 "out.png") at ../../src/export-image.c:87
#11 0x000055555558208e in main (argc=0x5, argv=0x7fffffffdd88) at ../../src/main.c:1123

gef➤  p  2.0/27.0 * pow (sin (angle / 4), 6) / pow (cos (angle / 4), 2)
$6 = -nan(0x8000000000000)
gef➤  p angle
$7 = 1.1632860543944119e-07
```

### src 

```
   do {
	angle = M_PI / i++;
	error = _arc_error_normalized (angle);
    } while (error > tolerance);   // error= 0 tolerance =0 ,so the loop will always be true.


```



