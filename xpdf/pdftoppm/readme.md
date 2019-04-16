
# Description
Xpdf is a free PDF viewer and toolkit, including a text extractor, image converter, HTML converter, and more.
# version
None

# others
## @_@
this bug is reported by fish@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detail


# [vuln/SplashXPath::strokeAdjust@SplashXPath.cc-245___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gdb info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (76127): Dictionary key must be a name object
Syntax Error (76129): Dictionary key must be a name object
Syntax Error (76133): Dictionary key must be a name object
Syntax Error (76144): Dictionary key must be a name object
Syntax Error (76150): Dictionary key must be a name object
Syntax Error (69485): Dictionary key must be a name object
Syntax Error (69487): Dictionary key must be a name object
Syntax Error (70398): Dictionary key must be a name object
Syntax Error (70404): Dictionary key must be a name object
Syntax Error (68761): Unknown operator 'x<9c><c5><92>KO<02>1<14><85><f7><f3>+<ce>R<17>^n<db><b9>mg<a9><f2><88>,<8c><8f><ee><08><0b><9c><01><82>2'
Syntax Error: Unterminated string
Syntax Error (2271): Unknown operator 'r'

......

too many Syntax Error
......

Syntax Error (4447): Too many args in content stream
Syntax Error (4447): Too many args in content stream
Syntax Error (4453): Too many args in content stream
Syntax Error (4453): Too many args in content stream
Syntax Error (4455): Too many args in content stream
Syntax Error (4486): Unknown operator 'p.9001869021'
Syntax Error (4503): Unknown operator 'c31235049.8701'
Syntax Error (4531): Unknown operator 'E453208'
Syntax Error (4562): Unknown operator 'E40.4000947719.475.455315062.5017'
=================================================================
==101442==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7f336e2e77f0 at pc 0x560b53b4ab1f bp 0x7ffca6c33a90 sp 0x7ffca6c33a80
READ of size 8 at 0x7f336e2e77f0 thread T0
    #0 0x560b53b4ab1e in SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:245
    #1 0x560b53b490d6 in SplashXPath::SplashXPath(SplashPath*, double*, double, int, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:101
    #2 0x560b53b07934 in Splash::fillWithPattern(SplashPath*, int, SplashPattern*, double) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2935
    #3 0x560b53b04b75 in Splash::strokeWide(SplashPath*, double, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2611
    #4 0x560b53b0345d in Splash::stroke(SplashPath*) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2467
    #5 0x560b538d2589 in SplashOutputDev::stroke(GfxState*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:1640
    #6 0x560b5394cc55 in Gfx::opStroke(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1652
    #7 0x560b5394466f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #8 0x560b53943c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #9 0x560b53943289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #10 0x560b53a396eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #11 0x560b53a38f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #12 0x560b53a3f380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #13 0x560b538f3485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #14 0x7f3372673b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #15 0x560b538c64b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x7f336e2e77f0 is located 16 bytes to the left of 1311568-byte region [0x7f336e2e7800,0x7f336e427b50)
allocated by thread T0 here:
    #0 0x7f3373714b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x560b53aabcc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x560b53aabe27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x560b53b48ed1 in SplashXPath::SplashXPath(SplashPath*, double*, double, int, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:93
    #4 0x560b53b07934 in Splash::fillWithPattern(SplashPath*, int, SplashPattern*, double) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2935
    #5 0x560b53b04b75 in Splash::strokeWide(SplashPath*, double, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2611
    #6 0x560b53b0345d in Splash::stroke(SplashPath*) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2467
    #7 0x560b538d2589 in SplashOutputDev::stroke(GfxState*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:1640
    #8 0x560b5394cc55 in Gfx::opStroke(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1652
    #9 0x560b5394466f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #10 0x560b53943c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #11 0x560b53943289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #12 0x560b53a396eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #13 0x560b53a38f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #14 0x560b53a3f380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #15 0x560b538f3485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #16 0x7f3372673b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:245 in SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode)
Shadow bytes around the buggy address:
  0x0fe6edc54ea0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fe6edc54eb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fe6edc54ec0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fe6edc54ed0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fe6edc54ee0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0fe6edc54ef0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]fa
  0x0fe6edc54f00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe6edc54f10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe6edc54f20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe6edc54f30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe6edc54f40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==101442==ABORTING

```


# [vuln/DCTStream::readScan@Stream.cc-3051___out-of-bounds-read](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

backtrace:
#0  0x000055555569b59b in DCTStream::readScan (this=0x5555559f1830)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3051
#1  0x000055555569980c in DCTStream::reset (this=0x5555559f1830)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2709
#2  0x00005555556932eb in ImageStream::reset (this=0x5555559f3c70)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:389
#3  0x00005555555f4a6f in SplashOutputDev::drawImage (this=0x5555559e15b0, 
    state=0x5555559f0ae0, ref=0x7fffffffd5e0, str=0x5555559f1830, width=0x1d8, 
    height=0x1d8, colorMap=0x5555559f3430, maskColors=0x0, inlineImg=0x0, 
    interpolate=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3466
#4  0x0000555555636f4e in Gfx::doImage (this=0x5555559d87e0, 
    ref=0x7fffffffd5e0, str=0x5555559f1830, inlineImg=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
#5  0x0000555555634f55 in Gfx::opXObject (this=0x5555559d87e0, 
    args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
#6  0x00005555556235c2 in Gfx::execOp (this=0x5555559d87e0, 
    cmd=0x7fffffffd6b0, args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
#7  0x000055555562303a in Gfx::go (this=0x5555559d87e0, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
#8  0x0000555555622afe in Gfx::display (this=0x5555559d87e0, 
    objRef=0x5555559e0ba0, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
#9  0x000055555568c91c in Page::displaySlice (this=0x5555559e0b70, 
    out=0x5555559e15b0, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x0, sliceX=0xffffffff, sliceY=0xffffffff, sliceW=0xffffffff, 
    sliceH=0xffffffff, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
#10 0x000055555568c4e5 in Page::display (this=0x5555559e0b70, 
    out=0x5555559e15b0, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x1, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
#11 0x000055555568f59a in PDFDoc::displayPage (this=0x5555559d6880, 
    out=0x5555559e15b0, page=0x1, hDPI=150, vDPI=150, rotate=0x0, 
    useMediaBox=0x0, crop=0x1, printing=0x0, abortCheckCbk=0x0, 
    abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
#12 0x00005555555f9ec8 in main (argc=0x3, argv=0x7fffffffdce8)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
#13 0x00007ffff6e12b97 in __libc_start_main (
    main=0x5555555f9917 <main(int, char**)>, argc=0x5, argv=0x7fffffffdce8, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffdcd8) at ../csu/libc-start.c:310
#14 0x00005555555e6a8a in _start ()

src info:
3046		  for (x2 = 0; x2 < dx1; x2 += horiz) {
3047	
3048		    // pull out the current values
3049		    p1 = &frameBuf[cc][(y1+y2) * bufWidth + (x1+x2)];
3050		    for (y3 = 0, i = 0; y3 < 8; ++y3, i += 8) {
3051		      data[i] = p1[0];
3052		      data[i+1] = p1[1];
3053		      data[i+2] = p1[2];
3054		      data[i+3] = p1[3];
3055		      data[i+4] = p1[4];

register info:
rax            0x0	0x0
rbx            0x5555559f3c70	0x5555559f3c70
rcx            0x0	0x0
rdx            0x0	0x0
rsi            0x0	0x0
rdi            0x5555559f1830	0x5555559f1830
rbp            0x7fffffffd0b0	0x7fffffffd0b0
rsp            0x7fffffffcf40	0x7fffffffcf40
r8             0x7fffffffcfa0	0x7fffffffcfa0
r9             0x5555559f16e8	0x5555559f16e8
r10            0x5555559d5bb0	0x5555559d5bb0
r11            0x246	0x246
r12            0x1	0x1
r13            0x8	0x8
r14            0x0	0x0
r15            0x0	0x0
rip            0x55555569b59b	0x55555569b59b <DCTStream::readScan()+977>
eflags         0x10297	[ CF PF AF SF IF RF ]
cs             0x33	0x33
ss             0x2b	0x2b
ds             0x0	0x0
es             0x0	0x0
fs             0x0	0x0
gs             0x0	0x0

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (78979): Illegal character <1d> in hex string
Syntax Error (78980): Illegal character <1d> in hex string
Syntax Error (78981): Illegal character <1d> in hex string
Syntax Error (78982): Illegal character <1d> in hex string
Syntax Error (78983): Illegal character <1d> in hex string
Syntax Error (78984): Illegal character <1d> in hex string
Syntax Error (78985): Illegal character <1d> in hex string
Syntax Error (78986): Illegal character <1d> in hex string
Syntax Error (78987): Illegal character <1d> in hex string
Syntax Error (78988): Illegal character <1d> in hex string
Syntax Error (78989): Illegal character <1d> in hex string
Syntax Error (78990): Illegal character <1d> in hex string
Syntax Error (78991): Illegal character <1d> in hex string
Syntax Error (78992): Illegal character <1d> in hex string
Syntax Error (78993): Illegal character <1d> in hex string
Syntax Error (78994): Illegal character <1d> in hex string
Syntax Error (78995): Illegal character <1d> in hex string
Syntax Error (78996): Illegal character <1d> in hex string
ASAN:DEADLYSIGNAL
=================================================================
==101608==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x55d5773b9656 bp 0x7fffabbf6980 sp 0x7fffabbf67a0 T0)
==101608==The signal is caused by a READ memory access.
==101608==Hint: address points to the zero page.
    #0 0x55d5773b9655 in DCTStream::readScan() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3051
    #1 0x55d5773b400b in DCTStream::reset() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2709
    #2 0x55d5773a1c65 in ImageStream::reset() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:389
    #3 0x55d577240952 in SplashOutputDev::drawImage(GfxState*, Object*, Stream*, int, int, GfxImageColorMap*, int*, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3466
    #4 0x55d5772c8b6d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
    #5 0x55d5772c5ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #6 0x55d57729f66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #7 0x55d57729ec71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #8 0x55d57729e289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #9 0x55d5773946eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #10 0x55d577393f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #11 0x55d57739a380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #12 0x55d57724e485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #13 0x7f46b2eb8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x55d5772214b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3051 in DCTStream::readScan()
==101608==ABORTING

```


# [vuln/CCITTFaxStream::readRow@Stream.cc-1822___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (11874): Dictionary key must be a name object
Syntax Error (11881): Illegal character '>'
Syntax Error (11883): Dictionary key must be a name object
Syntax Error (11894): Dictionary key must be a name object
Syntax Error (61): Illegal character '>'
Syntax Error (64): Dictionary key must be a name object
Syntax Error (840): Unknown operator '?<ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><fc>'

.......


Syntax Error (840): Unknown operator '<7f><ff><ff><c0>'
Syntax Error (840): Unknown operator '<ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><f0>'
yntax Error (910): Unknown operator '<01><ff><ff><ff><ff><c0>'
Syntax Error (919): CCITTFax row is wrong length (831)
Syntax Error (919): Unknown operator '<0f><ff><ff>'
Syntax Error (919): Unknown operator '<01><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><fc><1f><e0>'
Syntax Error (926): Unknown operator '<ff><ff><ff><ff><ff><ff><f0><1f><c0>'
Syntax Error (926): Unknown operator '<01><80>'
Syntax Error (926): Unknown operator '?<1f><ff><ff><ff><fe><07><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><f8><f0><ff><ff><ff><ff><ff><f0><1f><e0>'
=================================================================
==101826==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d000007640 at pc 0x55f8d96ac8a6 bp 0x7fff1d5e7610 sp 0x7fff1d5e7600
READ of size 4 at 0x61d000007640 thread T0
    #0 0x55f8d96ac8a5 in CCITTFaxStream::readRow() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1822
    #1 0x55f8d96aafc6 in CCITTFaxStream::getChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1605
    #2 0x55f8d9688c49 in Object::streamGetChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:300
    #3 0x55f8d967d10f in Lexer::getChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:93
    #4 0x55f8d967d2cf in Lexer::getObj(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:125
    #5 0x55f8d969624d in Parser::shift() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:268
    #6 0x55f8d9695583 in Parser::getObj(Object*, int, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:146
    #7 0x55f8d959cf25 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:751
    #8 0x55f8d959c289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #9 0x55f8d96926eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #10 0x55f8d9691f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #11 0x55f8d9698380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #12 0x55f8d954c485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #13 0x7f38954a9b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x55f8d951f4b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x61d000007640 is located 4 bytes to the right of 1980-byte region [0x61d000006e80,0x61d00000763c)
allocated by thread T0 here:
    #0 0x7f389654ab50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x55f8d9704cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x55f8d9704e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x55f8d96aa3b9 in CCITTFaxStream::CCITTFaxStream(Stream*, int, int, int, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1549
    #4 0x55f8d96aaa71 in CCITTFaxStream::copy() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1568
    #5 0x55f8d96869a3 in Object::copy(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:95
    #6 0x55f8d9686b4b in Object::fetch(XRef*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:114
    #7 0x55f8d95673d3 in Array::get(int, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Array.cc:62
    #8 0x55f8d967cf84 in Lexer::Lexer(XRef*, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:74
    #9 0x55f8d959c1e4 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:640
    #10 0x55f8d96926eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #11 0x55f8d9691f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #12 0x55f8d9698380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #13 0x55f8d954c485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #14 0x7f38954a9b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1822 in CCITTFaxStream::readRow()
Shadow bytes around the buggy address:
  0x0c3a7fff8e70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8e80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8e90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8ea0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8eb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fff8ec0: 00 00 00 00 00 00 00 04[fa]fa fa fa fa fa fa fa
  0x0c3a7fff8ed0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8ee0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8ef0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8f00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8f10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==101826==ABORTING

```


# [vuln/SplashXPath::strokeAdjust@SplashXPath.cc-246___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (112733): Dictionary key must be a name object
Syntax Error (112735): Dictionary key must be a name object
Syntax Error (112741): Dictionary key must be a name object
Syntax Error (112743): Dictionary key must be a name object

......

Syntax Error (2300): Arg #0 to 'Tf' operator is wrong type (real)
Syntax Error (2303): Too few (1) args to 'Tf' operator
Syntax Error (2303): Unknown operator 'EG'
Syntax Error (2311): Unknown operator 'Er000008'
Syntax Error (2312): Unknown operator 'r'
Syntax Error (2323): Unknown operator 'w3.2'
Syntax Error (2367): Unknown operator 'TJ3.22.4254'
Syntax Warning (2371): Badly formatted number
Syntax Error (2386): Too few (4) args to 'c' operator
=================================================================
==102074==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61e00000a680 at pc 0x55e706ae3bb5 bp 0x7fff2415d370 sp 0x7fff2415d360
READ of size 8 at 0x61e00000a680 thread T0
    #0 0x55e706ae3bb4 in SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:246
    #1 0x55e706ae20d6 in SplashXPath::SplashXPath(SplashPath*, double*, double, int, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:101
    #2 0x55e706aa0934 in Splash::fillWithPattern(SplashPath*, int, SplashPattern*, double) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2935
    #3 0x55e706a9db75 in Splash::strokeWide(SplashPath*, double, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2611
    #4 0x55e706a9c45d in Splash::stroke(SplashPath*) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2467
    #5 0x55e70686b589 in SplashOutputDev::stroke(GfxState*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:1640
    #6 0x55e7068e5c55 in Gfx::opStroke(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1652
    #7 0x55e7068dd66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #8 0x55e7068dcc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #9 0x55e7068dc289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #10 0x55e7069d26eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #11 0x55e7069d1f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #12 0x55e7069d8380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #13 0x55e70688c485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #14 0x7f161bc33b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #15 0x55e70685f4b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x61e00000a680 is located 0 bytes to the right of 2560-byte region [0x61e000009c80,0x61e00000a680)
allocated by thread T0 here:
    #0 0x7f161ccd4b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x55e706a44cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x55e706a44e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x55e706ae1ed1 in SplashXPath::SplashXPath(SplashPath*, double*, double, int, int, SplashStrokeAdjustMode) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:93
    #4 0x55e706aa0934 in Splash::fillWithPattern(SplashPath*, int, SplashPattern*, double) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2935
    #5 0x55e706a9db75 in Splash::strokeWide(SplashPath*, double, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2611
    #6 0x55e706a9c45d in Splash::stroke(SplashPath*) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:2467
    #7 0x55e70686b589 in SplashOutputDev::stroke(GfxState*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:1640
    #8 0x55e7068e5c55 in Gfx::opStroke(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1652
    #9 0x55e7068dd66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #10 0x55e7068dcc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #11 0x55e7068dc289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #12 0x55e7069d26eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #13 0x55e7069d1f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #14 0x55e7069d8380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #15 0x55e70688c485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #16 0x7f161bc33b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/SplashXPath.cc:246 in SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode)
Shadow bytes around the buggy address:
  0x0c3c7fff9480: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3c7fff9490: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3c7fff94a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3c7fff94b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3c7fff94c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3c7fff94d0:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff94e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff94f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9500: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9510: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9520: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==102074==ABORTING

```


# [vuln/CCITTFaxStream::readRow@Stream.cc-1861___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Warning: May not be a PDF file (continuing anyway)
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (3029): Missing 'endstream'
Syntax Error (3034): Illegal character ')'
Syntax Error (3144): Illegal character '>'
Syntax Error: End of file inside array
Syntax Error: End of file inside dictionary
Syntax Error (3029): Missing 'endstream'
Syntax Error: Page tree reference is wrong type (cmd)
Syntax Error: Page tree reference is wrong type (name)

......

Syntax Error: Page tree reference is wrong type (cmd)
Syntax Error: Page tree reference is wrong type (integer)
Syntax Error: Page tree reference is wrong type (integer)
Syntax Error: Page tree reference is wrong type (cmd)
Syntax Error: Page tree reference is wrong type (cmd)
Syntax Error: Page tree reference is wrong type (dictionary)
Syntax Error: Page tree reference is wrong type (cmd)
Syntax Error: Page tree reference is wrong type (integer)
=================================================================
==102139==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d000006c3c at pc 0x56014afe162b bp 0x7ffef65686c0 sp 0x7ffef65686b0
READ of size 4 at 0x61d000006c3c thread T0
    #0 0x56014afe162a in CCITTFaxStream::readRow() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1861
    #1 0x56014afdf9f0 in CCITTFaxStream::getBlock(char*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1687
    #2 0x56014afd4032 in ImageStream::getLine() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:418
    #3 0x56014ae70eba in SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3280
    #4 0x56014b0a7132 in Splash::upscaleImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, int, double*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4640
    #5 0x56014b0a464e in Splash::drawImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, double*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4452
    #6 0x56014ae7326e in SplashOutputDev::drawImage(GfxState*, Object*, Stream*, int, int, GfxImageColorMap*, int*, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3525
    #7 0x56014aefab6d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
    #8 0x56014aef7ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #9 0x56014aed166f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #10 0x56014aed0c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #11 0x56014aed0289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #12 0x56014afc66eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #13 0x56014afc5f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #14 0x56014afcc380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #15 0x56014ae80485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #16 0x7f6966f95b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #17 0x56014ae534b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x61d000006c3c is located 0 bytes to the right of 1980-byte region [0x61d000006480,0x61d000006c3c)
allocated by thread T0 here:
    #0 0x7f6968036b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x56014b038cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x56014b038e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x56014afde3b9 in CCITTFaxStream::CCITTFaxStream(Stream*, int, int, int, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1549
    #4 0x56014afd2cfc in Stream::makeFilter(char*, Stream*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:265
    #5 0x56014afd220d in Stream::addFilters(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:146
    #6 0x56014afc9f4c in Parser::makeStream(Object*, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:245
    #7 0x56014afc9152 in Parser::getObj(Object*, int, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:104
    #8 0x56014b024682 in XRef::fetch(int, int, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/XRef.cc:1086
    #9 0x56014afbab36 in Object::fetch(XRef*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:114
    #10 0x56014aebdacf in Dict::lookup(char const*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Dict.cc:125
    #11 0x56014afbc820 in Object::dictLookup(char const*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:267
    #12 0x56014aecdc42 in GfxResources::lookupXObject(char const*, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:374
    #13 0x56014aef785a in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3950
    #14 0x56014aed166f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #15 0x56014aed0c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #16 0x56014aed0289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #17 0x56014afc66eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #18 0x56014afc5f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #19 0x56014afcc380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #20 0x56014ae80485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #21 0x7f6966f95b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1861 in CCITTFaxStream::readRow()
Shadow bytes around the buggy address:
  0x0c3a7fff8d30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8d40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8d50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8d60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8d70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fff8d80: 00 00 00 00 00 00 00[04]fa fa fa fa fa fa fa fa
  0x0c3a7fff8d90: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8da0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8db0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8dc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8dd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==102139==ABORTING

```


# [vuln/Object::isName@Object.h-134___stack-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (78201): Illegal character <1d> in hex string
Syntax Error (78202): Illegal character <1d> in hex string
Syntax Error (78203): Illegal character <1d> in hex string
Syntax Error (78204): Illegal character <1d> in hex string
Syntax Error (78205): Illegal character <1d> in hex string
......

Syntax Error: Unknown shading 'Sh14'
Syntax Error: Unknown shading 'Sh15'
Syntax Error: Expected function dictionary or stream
Syntax Error: Unknown shading 'Sh16'
Syntax Error: Unknown shading 'Sh17'
Syntax Error: Unknown shading 'Sh18'
Syntax Error: Bad color space 'DeviceGhay'
Syntax Error: Unknown shading 'Sh19'
Syntax Error: Unknown shading 'Sh20'
Syntax Error: Unknown shading 'Sh21'
Syntax Error (63005): Illegal character '}'
Syntax Error: Expected function dictionary or stream
Syntax Error (63454): Unknown operator 'V<19>46'
=================================================================
==102382==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffd39389210 at pc 0x55f0800c7d7f bp 0x7ffd39388fb0 sp 0x7ffd39388fa0
READ of size 4 at 0x7ffd39389210 thread T0
    #0 0x55f0800c7d7e in Object::isName() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:134
    #1 0x55f07ffe4416 in Gfx::opSetFillColorN(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1479
    #2 0x55f07ffdd66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #3 0x55f07ffdcc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #4 0x55f07ffdc289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #5 0x55f080008d25 in Gfx::drawForm(Object*, Dict*, double*, double*, int, int, GfxColorSpace*, int, int, int, Function*, GfxColor*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4662
    #6 0x55f07ffe11a6 in Gfx::doSoftMask(Object*, Object*, int, GfxColorSpace*, int, int, Function*, GfxColor*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1257
    #7 0x55f07ffe08c8 in Gfx::opSetExtGState(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:1173
    #8 0x55f07ffdd66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #9 0x55f07ffdcc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #10 0x55f07ffdc289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #11 0x55f0800d26eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #12 0x55f0800d1f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #13 0x55f0800d8380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #14 0x55f07ff8c485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #15 0x7f6ed175bb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #16 0x55f07ff5f4b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

Address 0x7ffd39389210 is located in stack of thread T0 at offset 80 in frame
    #0 0x55f07ffdc7d3 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:683

  This frame has 2 object(s):
    [32, 48) 'obj'
    [96, 624) 'args' <== Memory access at offset 80 underflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:134 in Object::isName()
Shadow bytes around the buggy address:
  0x1000272691f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269200: 00 00 f1 f1 f1 f1 00 00 00 00 00 00 00 00 00 00
  0x100027269210: 00 00 00 00 00 00 f3 f3 f3 f3 00 00 00 00 00 00
  0x100027269220: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269230: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 00 00 f2 f2
=>0x100027269240: f2 f2[f2]f2 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269250: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269260: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269270: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100027269280: 00 00 00 00 00 00 f2 f2 00 00 00 00 00 00 00 00
  0x100027269290: 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1 00 00
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
==102382==ABORTING

```


# [vuln/DCTStream::getBlock@Stream.cc-2812___out-of-bounds-read](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

backtrace:
#0  0x0000555555699d9c in DCTStream::getBlock (this=0x5555559f1c10, 
    blk=0x5555559f4090 "R\314\035\367\377\177", size=0x1d8)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2812
#1  0x00005555556933ec in ImageStream::getLine (this=0x5555559f4050)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:418
#2  0x00005555555f4301 in SplashOutputDev::imageSrc (data=0x7fffffffd190, 
    colorLine=0x555555a1be40 "", alphaLine=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3280
#3  0x00005555556effb3 in Splash::scaleImageYdXd (this=0x5555559dd9e0, 
    src=0x5555555f42c4 <SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*)>, srcData=0x7fffffffd190, srcMode=splashModeRGB8, nComps=0x3, 
    srcAlpha=0x0, srcWidth=0x1d8, srcHeight=0x1d8, scaledWidth=0x59, 
    scaledHeight=0x59, dest=0x5555559f00e0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:5113
#4  0x00005555556efcea in Splash::scaleImage (this=0x5555559dd9e0, 
    src=0x5555555f42c4 <SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*)>, srcData=0x7fffffffd190, srcMode=splashModeRGB8, nComps=0x3, 
    srcAlpha=0x0, srcWidth=0x1d8, srcHeight=0x1d8, scaledWidth=0x59, 
    scaledHeight=0x59, interpolate=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:5034
#5  0x00005555556ec774 in Splash::drawImage (this=0x5555559dd9e0, 
    src=0x5555555f42c4 <SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*)>, srcData=0x7fffffffd190, srcMode=splashModeRGB8, srcAlpha=0x0, 
    w=0x1d8, h=0x1d8, mat=0x7fffffffd1d0, interpolate=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4465
#6  0x00005555555f4d8e in SplashOutputDev::drawImage (this=0x5555559dd870, 
    state=0x5555559f0ec0, ref=0x7fffffffd5e0, str=0x5555559f1c10, width=0x1d8, 
    height=0x1d8, colorMap=0x5555559f3810, maskColors=0x0, inlineImg=0x0, 
    interpolate=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3525
#7  0x0000555555636f4e in Gfx::doImage (this=0x5555559d9b20, 
    ref=0x7fffffffd5e0, str=0x5555559f1c10, inlineImg=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
#8  0x0000555555634f55 in Gfx::opXObject (this=0x5555559d9b20, 
    args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
#9  0x00005555556235c2 in Gfx::execOp (this=0x5555559d9b20, 
    cmd=0x7fffffffd6b0, args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
#10 0x000055555562303a in Gfx::go (this=0x5555559d9b20, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
#11 0x0000555555622afe in Gfx::display (this=0x5555559d9b20, 
    objRef=0x5555559dcdb0, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
#12 0x000055555568c91c in Page::displaySlice (this=0x5555559dcd80, 
    out=0x5555559dd870, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x0, sliceX=0xffffffff, sliceY=0xffffffff, sliceW=0xffffffff, 
    sliceH=0xffffffff, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
#13 0x000055555568c4e5 in Page::display (this=0x5555559dcd80, 
    out=0x5555559dd870, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x1, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
#14 0x000055555568f59a in PDFDoc::displayPage (this=0x5555559d6880, 
    out=0x5555559dd870, page=0x1, hDPI=150, vDPI=150, rotate=0x0, 
    useMediaBox=0x0, crop=0x1, printing=0x0, abortCheckCbk=0x0, 
    abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
#15 0x00005555555f9ec8 in main (argc=0x3, argv=0x7fffffffdce8)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
#16 0x00007ffff6e12b97 in __libc_start_main (
    main=0x5555555f9917 <main(int, char**)>, argc=0x5, argv=0x7fffffffdce8, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffdcd8) at ../csu/libc-start.c:310
#17 0x00005555555e6a8a in _start ()

src info:
2807	  if (progressive || !interleaved) {
2808	    if (y >= height) {
2809	      return 0;
2810	    }
2811	    for (nRead = 0; nRead < size; ++nRead) {
2812	      blk[nRead] = (char)frameBuf[comp][y * bufWidth + x];
2813	      if (++comp == numComps) {
2814		comp = 0;
2815		if (++x == width) {
2816		  x = 0;

register info:
rax            0x0	0x0
rbx            0x5555559f00e0	0x5555559f00e0
rcx            0x0	0x0
rdx            0x0	0x0
rsi            0x5555559f4090	0x5555559f4090
rdi            0x5555559f1c10	0x5555559f1c10
rbp            0x7fffffffcde0	0x7fffffffcde0
rsp            0x7fffffffcdb0	0x7fffffffcdb0
r8             0x77	0x77
r9             0x0	0x0
r10            0xfffffffffffff000	0xfffffffffffff000
r11            0x555555a1d000	0x555555a1d000
r12            0x1	0x1
r13            0x8	0x8
r14            0x0	0x0
r15            0x0	0x0
rip            0x555555699d9c	0x555555699d9c <DCTStream::getBlock(char*, int)+164>
eflags         0x10246	[ PF ZF IF RF ]
cs             0x33	0x33
ss             0x2b	0x2b
ds             0x0	0x0
es             0x0	0x0
fs             0x0	0x0
gs             0x0	0x0

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (1622): Dictionary key must be a name object
Syntax Error (1627): Dictionary key must be a name object
Syntax Error (1628): Illegal character '{'
Syntax Error (1628): Dictionary key must be a name object
Syntax Error (1646): Dictionary key must be a name object
Syntax Error (1657): Dictionary key must be a name object
Syntax Error (1658): Illegal character '{'
Syntax Error (1658): Dictionary key must be a name object
Syntax Error (1666): Dictionary key must be a name object
Syntax Error (1684): Dictionary key must be a name object
Syntax Error (1694): Dictionary key must be a name object
Syntax Error (1710): Illegal character ')'
Syntax Error (1713): Dictionary key must be a name object
Syntax Error (1714): Dictionary key must be a name object
Syntax Error (1723): Dictionary key must be a name object
Syntax Error (1739): Dictionary key must be a name object
Syntax Error (1742): Dictionary key must be a name object
Syntax Error (3562): Bad DCT data: missing 00 after ff
Syntax Error (4387): Bad Huffman code in DCT stream
Syntax Error (9875): Bad Huffman code in DCT stream
Syntax Error (14305): Bad number of components in DCT stream
ASAN:DEADLYSIGNAL
=================================================================
==102453==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x55c0e1b3b56f bp 0x7ffd589d2260 sp 0x7ffd589d2230 T0)
==102453==The signal is caused by a READ memory access.
==102453==Hint: address points to the zero page.
    #0 0x55c0e1b3b56e in DCTStream::getBlock(char*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2812
    #1 0x55c0e1b28032 in ImageStream::getLine() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:418
    #2 0x55c0e19c4eba in SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3280
    #3 0x55c0e1c00fb0 in Splash::scaleImageYdXd(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, int, int, int, SplashBitmap*) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:5113
    #4 0x55c0e1c00c97 in Splash::scaleImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:5034
    #5 0x55c0e1bf8b5a in Splash::drawImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, double*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4465
    #6 0x55c0e19c726e in SplashOutputDev::drawImage(GfxState*, Object*, Stream*, int, int, GfxImageColorMap*, int*, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3525
    #7 0x55c0e1a4eb6d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
    #8 0x55c0e1a4bba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #9 0x55c0e1a2566f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #10 0x55c0e1a24c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #11 0x55c0e1a24289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #12 0x55c0e1b1a6eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #13 0x55c0e1b19f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #14 0x55c0e1b20380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #15 0x55c0e19d4485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #16 0x7fd8ebec8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #17 0x55c0e19a74b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2812 in DCTStream::getBlock(char*, int)
==102453==ABORTING

```


# [vuln/DCTStream::readHuffSym@Stream.cc-3662___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error: Page tree object is wrong type (null)
Syntax Error: Invalid page count in page tree
Syntax Error (77112): Dictionary key must be a name object
Syntax Error (77114): Dictionary key must be a name object
Syntax Error (77131): Dictionary key must be a name object
Syntax Warning: Unknown font type: '???'
Syntax Error (80989): Illegal character '{'
Syntax Warning: Non-CID font with DescendantFonts array
=================================================================
==102480==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x620000004f76 at pc 0x55c68513f81e bp 0x7ffe8c2d7b60 sp 0x7ffe8c2d7b50
READ of size 2 at 0x620000004f76 thread T0
    #0 0x55c68513f81d in DCTStream::readHuffSym(DCTHuffTable*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3662
    #1 0x55c685139812 in DCTStream::readDataUnit(DCTHuffTable*, DCTHuffTable*, int*, int*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3126
    #2 0x55c685135404 in DCTStream::readMCURow() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2894
    #3 0x55c685133c75 in DCTStream::getChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2774
    #4 0x55c685109c49 in Object::streamGetChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:300
    #5 0x55c6850fe10f in Lexer::getChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:93
    #6 0x55c6850fe2cf in Lexer::getObj(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:125
    #7 0x55c6851159db in Parser::Parser(XRef*, Lexer*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:35
    #8 0x55c68501d23a in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:640
    #9 0x55c6851136eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #10 0x55c685112f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #11 0x55c685119380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #12 0x55c684fcd485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #13 0x7f6ce0362b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x55c684fa04b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x620000004f76 is located 262 bytes to the right of 3568-byte region [0x620000004080,0x620000004e70)
allocated by thread T0 here:
    #0 0x7f6ce1405458 in operator new(unsigned long) (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xe0458)
    #1 0x55c685131e41 in DCTStream::copy() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2631
    #2 0x55c6851079a3 in Object::copy(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:95
    #3 0x55c685107b4b in Object::fetch(XRef*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:114
    #4 0x55c684fe83d3 in Array::get(int, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Array.cc:62
    #5 0x55c6850fdf84 in Lexer::Lexer(XRef*, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:74
    #6 0x55c68501d1e4 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:640
    #7 0x55c6851136eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #8 0x55c685112f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #9 0x55c685119380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #10 0x55c684fcd485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #11 0x7f6ce0362b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3662 in DCTStream::readHuffSym(DCTHuffTable*)
Shadow bytes around the buggy address:
  0x0c407fff8990: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c407fff89a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c407fff89b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c407fff89c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 fa fa
  0x0c407fff89d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c407fff89e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]fa
  0x0c407fff89f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c407fff8a00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c407fff8a10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c407fff8a20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c407fff8a30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==102480==ABORTING

```


# [vuln/CCITTFaxStream::readRow@Stream.cc-1851___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (12806): Dictionary key must be a name object
Syntax Error (12810): Dictionary key must be a name object

......

Syntax Error (813): Unknown operator '<08><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><fc>'
Syntax Error (821): CCITTFax row is wrong length (537)
Syntax Error (822): Unknown operator '<0f><ff><ff><f8>'
Syntax Error (822): Unknown operator '<07><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><ff><e0>'
Syntax Error (827): Bad black code (001a) in CCITTFax stream
Syntax Error (829): CCITTFax row is wrong length (2129)
Syntax Error (830): Unknown operator '<08><fc><1f><ff><fc>?<ff>?<c3><ff><ff><ff><fc>'
=================================================================
==102493==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d000009440 at pc 0x56334392d2cc bp 0x7ffcaf1fbb70 sp 0x7ffcaf1fbb60
READ of size 4 at 0x61d000009440 thread T0
    #0 0x56334392d2cb in CCITTFaxStream::readRow() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1851
    #1 0x56334392b536 in CCITTFaxStream::lookChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1645
    #2 0x563343908cdd in Object::streamLookChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:303
    #3 0x5633438fd2a7 in Lexer::lookChar() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:109
    #4 0x5633438fe34e in Lexer::getObj(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:489
    #5 0x56334391624d in Parser::shift() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:268
    #6 0x563343915583 in Parser::getObj(Object*, int, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:146
    #7 0x56334381cf25 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:751
    #8 0x56334381c289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #9 0x5633439126eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #10 0x563343911f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #11 0x563343918380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #12 0x5633437cc485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #13 0x7f1c707cbb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x56334379f4b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x61d000009440 is located 4 bytes to the right of 1980-byte region [0x61d000008c80,0x61d00000943c)
allocated by thread T0 here:
    #0 0x7f1c7186cb50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x563343984cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x563343984e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x56334392a3b9 in CCITTFaxStream::CCITTFaxStream(Stream*, int, int, int, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1549
    #4 0x56334392aa71 in CCITTFaxStream::copy() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1568
    #5 0x5633439069a3 in Object::copy(Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:95
    #6 0x563343906b4b in Object::fetch(XRef*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:114
    #7 0x5633437e73d3 in Array::get(int, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Array.cc:62
    #8 0x5633438fcf84 in Lexer::Lexer(XRef*, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Lexer.cc:74
    #9 0x56334381c1e4 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:640
    #10 0x5633439126eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #11 0x563343911f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #12 0x563343918380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #13 0x5633437cc485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #14 0x7f1c707cbb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1851 in CCITTFaxStream::readRow()
Shadow bytes around the buggy address:
  0x0c3a7fff9230: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff9240: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff9250: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff9260: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff9270: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fff9280: 00 00 00 00 00 00 00 04[fa]fa fa fa fa fa fa fa
  0x0c3a7fff9290: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff92a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff92b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff92c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff92d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==102493==ABORTING

```


# [vuln/DCTStream::decodeImage@Stream.cc-3325___out-of-bounds-read](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

backtrace:
#0  0x000055555569c67e in DCTStream::decodeImage (this=0x5555559f1830)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3325
#1  0x000055555569982f in DCTStream::reset (this=0x5555559f1830)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2713
#2  0x00005555556932eb in ImageStream::reset (this=0x5555559f3c70)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:389
#3  0x00005555555f4a6f in SplashOutputDev::drawImage (this=0x5555559e15b0, 
    state=0x5555559f0ae0, ref=0x7fffffffd5e0, str=0x5555559f1830, width=0x1d8, 
    height=0x1d8, colorMap=0x5555559f3430, maskColors=0x0, inlineImg=0x0, 
    interpolate=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3466
#4  0x0000555555636f4e in Gfx::doImage (this=0x5555559d9b20, 
    ref=0x7fffffffd5e0, str=0x5555559f1830, inlineImg=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
#5  0x0000555555634f55 in Gfx::opXObject (this=0x5555559d9b20, 
    args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
#6  0x00005555556235c2 in Gfx::execOp (this=0x5555559d9b20, 
    cmd=0x7fffffffd6b0, args=0x7fffffffd6c0, numArgs=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
#7  0x000055555562303a in Gfx::go (this=0x5555559d9b20, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
#8  0x0000555555622afe in Gfx::display (this=0x5555559d9b20, 
    objRef=0x5555559e0c70, topLevel=0x1)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
#9  0x000055555568c91c in Page::displaySlice (this=0x5555559e0c40, 
    out=0x5555559e15b0, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x0, sliceX=0xffffffff, sliceY=0xffffffff, sliceW=0xffffffff, 
    sliceH=0xffffffff, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
#10 0x000055555568c4e5 in Page::display (this=0x5555559e0c40, 
    out=0x5555559e15b0, hDPI=150, vDPI=150, rotate=0x0, useMediaBox=0x0, 
    crop=0x1, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
#11 0x000055555568f59a in PDFDoc::displayPage (this=0x5555559d6880, 
    out=0x5555559e15b0, page=0x1, hDPI=150, vDPI=150, rotate=0x0, 
    useMediaBox=0x0, crop=0x1, printing=0x0, abortCheckCbk=0x0, 
    abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
#12 0x00005555555f9ec8 in main (argc=0x3, argv=0x7fffffffdce8)
    at /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
#13 0x00007ffff6e12b97 in __libc_start_main (
    main=0x5555555f9917 <main(int, char**)>, argc=0x5, argv=0x7fffffffdce8, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffdcd8) at ../csu/libc-start.c:310
#14 0x00005555555e6a8a in _start ()

src info:
3320		  for (x2 = 0; x2 < mcuWidth; x2 += horiz) {
3321	
3322		    // pull out the coded data unit
3323		    p1 = &frameBuf[cc][(y1+y2) * bufWidth + (x1+x2)];
3324		    for (y3 = 0, i = 0; y3 < 8; ++y3, i += 8) {
3325		      dataIn[i]   = p1[0];
3326		      dataIn[i+1] = p1[1];
3327		      dataIn[i+2] = p1[2];
3328		      dataIn[i+3] = p1[3];
3329		      dataIn[i+4] = p1[4];

register info:
rax            0x0	0x0
rbx            0x5555559f3c70	0x5555559f3c70
rcx            0x0	0x0
rdx            0x0	0x0
rsi            0x0	0x0
rdi            0x80	0x80
rbp            0x7fffffffd0b0	0x7fffffffd0b0
rsp            0x7fffffffcec0	0x7fffffffcec0
r8             0x7ffff71de8b0	0x7ffff71de8b0
r9             0x7ffff7fce740	0x7ffff7fce740
r10            0xffffffd5	0xffffffd5
r11            0x246	0x246
r12            0x1	0x1
r13            0x8	0x8
r14            0x0	0x0
r15            0x0	0x0
rip            0x55555569c67e	0x55555569c67e <DCTStream::decodeImage()+578>
eflags         0x10297	[ CF PF AF SF IF RF ]
cs             0x33	0x33
ss             0x2b	0x2b
ds             0x0	0x0
es             0x0	0x0
fs             0x0	0x0
gs             0x0	0x0

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (50524): Illegal character <6e> in hex string
Syntax Error (50529): Illegal character <68> in hex string
Syntax Error (50531): Illegal character <72> in hex string
Syntax Error (40831): Dictionary key must be a name object
Syntax Error (40833): Dictionary key must be a name object
Syntax Error (40839): Dictionary key must be a name object
Syntax Error (2711): Bad DCT data: missing 00 after ff
Syntax Error (7880): Bad DCT data: missing 00 after ff
Syntax Error (9695): Invalid DCT component ID in scan info block
ASAN:DEADLYSIGNAL
=================================================================
==102671==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x56476fc2e588 bp 0x7ffe144be370 sp 0x7ffe144be0f0 T0)
==102671==The signal is caused by a READ memory access.
==102671==Hint: address points to the zero page.
    #0 0x56476fc2e587 in DCTStream::decodeImage() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3325
    #1 0x56476fc2602e in DCTStream::reset() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:2713
    #2 0x56476fc13c65 in ImageStream::reset() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:389
    #3 0x56476fab2952 in SplashOutputDev::drawImage(GfxState*, Object*, Stream*, int, int, GfxImageColorMap*, int*, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3466
    #4 0x56476fb3ab6d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
    #5 0x56476fb37ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #6 0x56476fb1166f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #7 0x56476fb10c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #8 0x56476fb10289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #9 0x56476fc066eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #10 0x56476fc05f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #11 0x56476fc0c380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #12 0x56476fac0485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #13 0x7f3a68a8db96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x56476fa934b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:3325 in DCTStream::decodeImage()
==102671==ABORTING

```


# [vuln/CCITTFaxStream::readRow@Stream.cc-1841___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (765): CCITTFax row is wrong length (495)
Syntax Error (769): CCITTFax row is wrong length (496)
Syntax Error (782): CCITTFax row is wrong length (495)
Syntax Error (790): CCITTFax row is wrong length (507)
Syntax Error (797): CCITTFax row is wrong length (494)
Syntax Error (803): CCITTFax row is wrong length (496)
=================================================================
==103128==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00000263c at pc 0x5621edb4df6a bp 0x7fff5ee87f60 sp 0x7fff5ee87f50
READ of size 4 at 0x61d00000263c thread T0
    #0 0x5621edb4df69 in CCITTFaxStream::readRow() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1841
    #1 0x5621edb4c9f0 in CCITTFaxStream::getBlock(char*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1687
    #2 0x5621edb41032 in ImageStream::getLine() /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:418
    #3 0x5621ed9ddeba in SplashOutputDev::imageSrc(void*, unsigned char*, unsigned char*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3280
    #4 0x5621edc14132 in Splash::upscaleImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, int, double*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4640
    #5 0x5621edc1164e in Splash::drawImage(int (*)(void*, unsigned char*, unsigned char*), void*, SplashColorMode, int, int, int, double*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/splash/Splash.cc:4452
    #6 0x5621ed9e026e in SplashOutputDev::drawImage(GfxState*, Object*, Stream*, int, int, GfxImageColorMap*, int*, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/SplashOutputDev.cc:3525
    #7 0x5621eda67b6d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4457
    #8 0x5621eda64ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #9 0x5621eda3e66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #10 0x5621eda3dc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #11 0x5621eda3d289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #12 0x5621edb336eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #13 0x5621edb32f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #14 0x5621edb39380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #15 0x5621ed9ed485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #16 0x7fb34cc0eb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #17 0x5621ed9c04b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x61d00000263c is located 0 bytes to the right of 1980-byte region [0x61d000001e80,0x61d00000263c)
allocated by thread T0 here:
    #0 0x7fb34dcafb50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x5621edba5cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x5621edba5e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x5621edb4b3b9 in CCITTFaxStream::CCITTFaxStream(Stream*, int, int, int, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1549
    #4 0x5621edb3fcfc in Stream::makeFilter(char*, Stream*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:265
    #5 0x5621edb3f20d in Stream::addFilters(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:146
    #6 0x5621edb36f4c in Parser::makeStream(Object*, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:245
    #7 0x5621edb36152 in Parser::getObj(Object*, int, unsigned char*, CryptAlgorithm, int, int, int, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Parser.cc:104
    #8 0x5621edb91682 in XRef::fetch(int, int, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/XRef.cc:1086
    #9 0x5621edb27b36 in Object::fetch(XRef*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.cc:114
    #10 0x5621eda2aacf in Dict::lookup(char const*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Dict.cc:125
    #11 0x5621edb29820 in Object::dictLookup(char const*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Object.h:267
    #12 0x5621eda3ac42 in GfxResources::lookupXObject(char const*, Object*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:374
    #13 0x5621eda6485a in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3950
    #14 0x5621eda3e66f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #15 0x5621eda3dc71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #16 0x5621eda3d289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #17 0x5621edb336eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #18 0x5621edb32f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #19 0x5621edb39380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #20 0x5621ed9ed485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #21 0x7fb34cc0eb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Stream.cc:1841 in CCITTFaxStream::readRow()
Shadow bytes around the buggy address:
  0x0c3a7fff8470: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8480: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8490: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff84a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff84b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fff84c0: 00 00 00 00 00 00 00[04]fa fa fa fa fa fa fa fa
  0x0c3a7fff84d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff84e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff84f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8500: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8510: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==103128==ABORTING

```


# [vuln/GfxImageColorMap::GfxImageColorMap@GfxState.cc-3550___heap-buffer-overflow](#description)
## target
```
pdftoppm -f 1 @@ /dev/null
```
## gd b info
```

src info:
79	   "configuration file to use in place of .xpdfrc"},
80	  {"-v",      argFlag,     &printVersion,  0,
81	   "print copyright and version info"},
82	  {"-h",      argFlag,     &printHelp,     0,
83	   "print usage information"},
84	  {"-help",   argFlag,     &printHelp,     0,
85	   "print usage information"},
86	  {"--help",  argFlag,     &printHelp,     0,
87	   "print usage information"},
88	  {"-?",      argFlag,     &printHelp,     0,

```
## asan report
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
Syntax Error (1303): Illegal character '>'
Syntax Error (1303): Dictionary key must be a name object
Syntax Error (1310): Dictionary key must be a name object
Syntax Error (1338): Dictionary key must be a name object
Syntax Error (1343): Dictionary key must be a name object
Syntax Error (1353): Dictionary key must be a name object
Syntax Error (1360): Dictionary key must be a name object
Syntax Error (1363): Dictionary key must be a name object
Syntax Error (1365): Dictionary key must be a name object
Syntax Error (1369): Dictionary key must be a name object
Syntax Error (1372): Dictionary key must be a name object
Syntax Error (1379): Dictionary key must be a name object
Syntax Error (1382): Dictionary key must be a name object
Syntax Error (1384): Dictionary key must be a name object
Syntax Error (1388): Dictionary key must be a name object
Syntax Error (1391): Dictionary key must be a name object
Syntax Error (1399): Dictionary key must be a name object
Syntax Error: Bad Indexed color space (lookup table string too short)
=================================================================
==103344==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200002284d at pc 0x55ce43058206 bp 0x7ffdbbcf6fd0 sp 0x7ffdbbcf6fc0
READ of size 1 at 0x60200002284d thread T0
    #0 0x55ce43058205 in GfxImageColorMap::GfxImageColorMap(int, Object*, GfxColorSpace*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/GfxState.cc:3550
    #1 0x55ce4301929d in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4215
    #2 0x55ce43017ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #3 0x55ce42ff166f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #4 0x55ce42ff0c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #5 0x55ce42ff0289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #6 0x55ce430e66eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #7 0x55ce430e5f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #8 0x55ce430ec380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #9 0x55ce42fa0485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #10 0x7f20a54f8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #11 0x55ce42f734b9 in _start (/home/fish/Desktop/2018-10-10/xpdf-4.00/asan/asan/bin/pdftoppm+0x1304b9)

0x60200002284d is located 3 bytes to the left of 12-byte region [0x602000022850,0x60200002285c)
allocated by thread T0 here:
    #0 0x7f20a6599b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x55ce43158cc7 in gmalloc /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:140
    #2 0x55ce43158e27 in gmallocn /home/fish/Desktop/2018-10-10/xpdf-4.00/goo/gmem.cc:206
    #3 0x55ce4303ba82 in GfxIndexedColorSpace::GfxIndexedColorSpace(GfxColorSpace*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/GfxState.cc:1032
    #4 0x55ce4303c1db in GfxIndexedColorSpace::parse(Array*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/GfxState.cc:1089
    #5 0x55ce43033edc in GfxColorSpace::parse(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/GfxState.cc:148
    #6 0x55ce430190ae in Gfx::doImage(Object*, Stream*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:4195
    #7 0x55ce43017ba5 in Gfx::opXObject(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:3980
    #8 0x55ce42ff166f in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:826
    #9 0x55ce42ff0c71 in Gfx::go(int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:719
    #10 0x55ce42ff0289 in Gfx::display(Object*, int) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Gfx.cc:641
    #11 0x55ce430e66eb in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:373
    #12 0x55ce430e5f2c in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/Page.cc:321
    #13 0x55ce430ec380 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/PDFDoc.cc:386
    #14 0x55ce42fa0485 in main /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/pdftoppm.cc:228
    #15 0x7f20a54f8b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/2018-10-10/xpdf-4.00/xpdf/GfxState.cc:3550 in GfxImageColorMap::GfxImageColorMap(int, Object*, GfxColorSpace*)
Shadow bytes around the buggy address:
  0x0c047fffc4b0: fa fa 00 00 fa fa 00 fa fa fa fd fa fa fa fd fa
  0x0c047fffc4c0: fa fa fd fa fa fa fd fa fa fa fd fa fa fa 05 fa
  0x0c047fffc4d0: fa fa fd fa fa fa fd fa fa fa fd fa fa fa fd fa
  0x0c047fffc4e0: fa fa fd fd fa fa fd fa fa fa 00 04 fa fa fd fa
  0x0c047fffc4f0: fa fa fd fa fa fa fd fd fa fa 06 fa fa fa fd fa
=>0x0c047fffc500: fa fa fd fd fa fa 00 00 fa[fa]00 04 fa fa fd fd
  0x0c047fffc510: fa fa fd fa fa fa fd fd fa fa fd fa fa fa fd fd
  0x0c047fffc520: fa fa fd fa fa fa fd fd fa fa 00 00 fa fa 00 00
  0x0c047fffc530: fa fa 00 00 fa fa 00 00 fa fa fa fa fa fa fa fa
  0x0c047fffc540: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fffc550: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==103344==ABORTING

```



Thanks for your watching 

This markdown is automatically made by pySpider

Data : 2018-10-16 11:03:00 

Author: fish

Team : 360TeamSeri0us 

