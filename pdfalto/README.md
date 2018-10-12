# Description

pdfalto is a command line executable for parsing PDF files and producing structured XML representations of the PDF content in ALTO format.

# version
 
0.2 release

# others

## @_@
this bug is reported by fish@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detail


# [vuln/TextPage::restoreState@XmlAltoOutputDev.cc-6211___out-of-bounds-read](#description)
## target
```
pdfalto TextPage::restoreState@XmlAltoOutputDev.cc-6211___out-of-bounds-read /tmp/out.xml
```
## gdb info
```

backtrace:
#0  0x00005555555c2e06 in TextPage::restoreState (this=0x5555573a3540, 
    state=0x5555573a7ea0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:6211
#1  0x00005555555c884e in XmlAltoOutputDev::restoreState (this=0x55555739f930, 
    state=0x5555573a7ea0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:7862
#2  0x000055555567d6d3 in Gfx::restoreState (this=0x555557396320)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:5131
#3  0x00005555556671f5 in Gfx::opRestore (this=0x555557396320, 
    args=0x7fffffffd5e0, numArgs=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:881
#4  0x0000555555666f90 in Gfx::execOp (this=0x555557396320, 
    cmd=0x7fffffffd5d0, args=0x7fffffffd5e0, numArgs=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:826
#5  0x0000555555666a08 in Gfx::go (this=0x555557396320, topLevel=0x1)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:719
#6  0x00005555556664da in Gfx::display (this=0x555557396320, 
    objRef=0x55555739ee30, topLevel=0x1)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:641
#7  0x0000555555616e66 in Page::displaySlice (this=0x55555739ee00, 
    out=0x55555739f930, hDPI=72, vDPI=72, rotate=0x0, useMediaBox=0x1, 
    crop=0x1, sliceX=0xffffffff, sliceY=0xffffffff, sliceW=0xffffffff, 
    sliceH=0xffffffff, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:373
#8  0x0000555555616a2f in Page::display (this=0x55555739ee00, 
    out=0x55555739f930, hDPI=72, vDPI=72, rotate=0x0, useMediaBox=0x1, 
    crop=0x1, printing=0x0, abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:321
#9  0x0000555555618c26 in PDFDoc::displayPage (this=0x555557395c98, 
    out=0x55555739f930, page=0x1, hDPI=72, vDPI=72, rotate=0x0, 
    useMediaBox=0x1, crop=0x1, printing=0x0, abortCheckCbk=0x0, 
    abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:386
#10 0x0000555555618cab in PDFDoc::displayPages (this=0x555557395c98, 
    out=0x55555739f930, firstPage=0x1, lastPage=0x1, hDPI=72, vDPI=72, 
    rotate=0x0, useMediaBox=0x1, crop=0x1, printing=0x0, abortCheckCbk=0x0, 
    abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:399
#11 0x00005555555ac6d2 in PDFDocXrce::displayPages (this=0x555557395c90, 
    out=0x55555739f930, docrootA=0x0, firstPage=0x1, lastPage=0x1, hDPI=72, 
    vDPI=72, rotate=0x0, useMediaBox=0x1, crop=0x1, doLinks=0x0, 
    abortCheckCbk=0x0, abortCheckCbkData=0x0)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/PDFDocXrce.cc:22
#12 0x00005555555ad74f in main (argc=0x3, argv=0x7fffffffddf8)
    at /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/pdfalto.cc:415
#13 0x00007ffff6b01b97 in __libc_start_main (
    main=0x5555555ac994 <main(int, char**)>, argc=0x3, argv=0x7fffffffddf8, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffdde8) at ../csu/libc-start.c:310
#14 0x00005555555a9bda in _start ()

src info:
6206	    idStack.push(idCur);
6207	}
6208	
6209	void TextPage::restoreState(GfxState *state) {
6210	
6211	    idCur = idStack.top();
6212	    idStack.pop();
6213	}
6214	
6215	void TextPage::doPathForClip(GfxPath *path, GfxState *state,

register info:
rax            0x2d38313000000200	0x2d38313000000200
rbx            0x7fffffffd800	0x7fffffffd800
rcx            0x0	0x0
rdx            0x2d38313000000200	0x2d38313000000200
rsi            0x55555739f1b0	0x55555739f1b0
rdi            0x7fffffffd460	0x7fffffffd460
rbp            0x7fffffffd4d0	0x7fffffffd4d0
rsp            0x7fffffffd4c0	0x7fffffffd4c0
r8             0x0	0x0
r9             0x0	0x0
r10            0x7ffff6c4a8b0	0x7ffff6c4a8b0
r11            0x246	0x246
r12            0x7fffffffd7f0	0x7fffffffd7f0
r13            0x55555739f3a0	0x55555739f3a0
r14            0x0	0x0
r15            0x0	0x0
rip            0x5555555c2e06	0x5555555c2e06 <TextPage::restoreState(GfxState*)+34>
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
Syntax Error (816): Missing 'endstream'
Syntax Error (810): Unknown operator ']'
Syntax Error (815): Too few (0) args to 'TJ' operator
Syntax Error (821): Unknown operator 'qre.1ro'
Syntax Error (821): Unknown operator 'ETe1dg2'
Syntax Error (822): Unknown operator 'p'
Syntax Error (827): Unknown operator 'pT'
Syntax Error (828): Too few (0) args to 'w' operator
Syntax Error (830): Unknown operator 'pT'
Syntax Error (831): Too few (0) args to 'w' operator
Syntax Error (833): Unknown operator 'pT'
Syntax Error (835): Too few (0) args to 'w' operator
Syntax Error (836): Unknown operator 'pT'
Syntax Error (837): Unknown operator 'w4'
Syntax Error (840): Unknown operator 'e'
Syntax Error (846): Unknown operator 'iP0p'
Syntax Error (850): Unknown operator 'T'
Syntax Error (851): Too few (0) args to 'w' operator
Syntax Error (852): Unknown operator 'pT'
Syntax Error (855): Unknown operator 'H'
Syntax Error (857): Unknown operator 'pT'
Syntax Error (858): Too few (0) args to 'w' operator
Syntax Error (865): Unknown operator 'pT'
Syntax Error (868): Unknown operator 'H6eweib1J'
Syntax Error (871): Unknown operator 'ws.'
Syntax Error (872): Too few (0) args to 'w' operator
Syntax Error (873): Unknown operator 'd7'
Syntax Error (876): Unknown operator 'e'
ASAN:DEADLYSIGNAL
=================================================================
==50732==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x562c45781be2 bp 0x7ffc3509a850 sp 0x7ffc3509a840 T0)
==50732==The signal is caused by a READ memory access.
==50732==Hint: address points to the zero page.
    #0 0x562c45781be1 in TextPage::restoreState(GfxState*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:6211
    #1 0x562c4578dfd8 in XmlAltoOutputDev::restoreState(GfxState*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:7862
    #2 0x562c459171b1 in Gfx::restoreState() /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:5131
    #3 0x562c458e753a in Gfx::opRestore(Object*, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:881
    #4 0x562c458e72ad in Gfx::execOp(Object*, Object*, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:826
    #5 0x562c458e68af in Gfx::go(int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:719
    #6 0x562c458e5ed5 in Gfx::display(Object*, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:641
    #7 0x562c4583d4b3 in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:373
    #8 0x562c4583ccf4 in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:321
    #9 0x562c45841630 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:386
    #10 0x562c458416b8 in PDFDoc::displayPages(OutputDev*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:399
    #11 0x562c457510d5 in PDFDocXrce::displayPages(OutputDev*, _xmlNode*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/PDFDocXrce.cc:22
    #12 0x562c457528f0 in main /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/pdfalto.cc:415
    #13 0x7fe662c5db96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x562c4574c909 in _start (/home/fish/Desktop/2018-09-25/pdfalto-0.2/asan/pdfalto+0x101909)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:6211 in TextPage::restoreState(GfxState*)
==50732==ABORTING

```


## target

./pdfalto poc_heap_buffer_overflow /tmp/out.xml


## asan report 

```

=================================================================
==51791==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000024fda at pc 0x7fcedb7d28f9 bp 0x7ffd7155e5b0 sp 0x7ffd7155dd40
WRITE of size 13 at 0x602000024fda thread T0
    #0 0x7fcedb7d28f8 in __interceptor_vsprintf (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x9e8f8)
    #1 0x7fcedb7d2c86 in __interceptor_sprintf (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x9ec86)
    #2 0x55ca8343f6e4 in TextPage::addAttributsNode(_xmlNode*, IWord*, double&, double&, double&, double&, double&, double&, TextFontStyleInfo*, UnicodeMap*, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:3107
    #3 0x55ca8344e085 in TextPage::dump(int, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:5198
    #4 0x55ca834615a8 in XmlAltoOutputDev::endPage() /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:7664
    #5 0x55ca835ba892 in Gfx::~Gfx() /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:590
    #6 0x55ca83512844 in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:406
    #7 0x55ca83511cf4 in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:321
    #8 0x55ca83516630 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:386
    #9 0x55ca835166b8 in PDFDoc::displayPages(OutputDev*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:399
    #10 0x55ca834260d5 in PDFDocXrce::displayPages(OutputDev*, _xmlNode*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/PDFDocXrce.cc:22
    #11 0x55ca834278f0 in main /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/pdfalto.cc:415
    #12 0x7fceda460b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #13 0x55ca83421909 in _start (/home/fish/Desktop/2018-09-25/pdfalto-0.2/asan/pdfalto+0x101909)

0x602000024fda is located 0 bytes to the right of 10-byte region [0x602000024fd0,0x602000024fda)
allocated by thread T0 here:
    #0 0x7fcedb812b50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x55ca8343ed4a in TextPage::addAttributsNode(_xmlNode*, IWord*, double&, double&, double&, double&, double&, double&, TextFontStyleInfo*, UnicodeMap*, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:2998
    #2 0x55ca8344e085 in TextPage::dump(int, int) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:5198
    #3 0x55ca834615a8 in XmlAltoOutputDev::endPage() /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/XmlAltoOutputDev.cc:7664
    #4 0x55ca835ba892 in Gfx::~Gfx() /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Gfx.cc:590
    #5 0x55ca83512844 in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:406
    #6 0x55ca83511cf4 in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/Page.cc:321
    #7 0x55ca83516630 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:386
    #8 0x55ca835166b8 in PDFDoc::displayPages(OutputDev*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/xpdf-4.00/xpdf/PDFDoc.cc:399
    #9 0x55ca834260d5 in PDFDocXrce::displayPages(OutputDev*, _xmlNode*, int, int, double, double, int, int, int, int, int (*)(void*), void*) /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/PDFDocXrce.cc:22
    #10 0x55ca834278f0 in main /home/fish/Desktop/2018-09-25/pdfalto-0.2/src/pdfalto.cc:415
    #11 0x7fceda460b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)

SUMMARY: AddressSanitizer: heap-buffer-overflow (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x9e8f8) in __interceptor_vsprintf
Shadow bytes around the buggy address:
  0x0c047fffc9a0: fa fa fd fa fa fa fd fa fa fa fd fd fa fa fd fa
  0x0c047fffc9b0: fa fa fd fa fa fa fd fa fa fa fd fd fa fa fd fa
  0x0c047fffc9c0: fa fa fd fa fa fa fd fa fa fa fd fa fa fa fd fa
  0x0c047fffc9d0: fa fa fd fa fa fa fd fa fa fa fd fd fa fa fd fa
  0x0c047fffc9e0: fa fa fd fd fa fa fd fa fa fa 00 03 fa fa 00 01
=>0x0c047fffc9f0: fa fa 00 02 fa fa 07 fa fa fa 00[02]fa fa fd fd
  0x0c047fffca00: fa fa fd fa fa fa fd fd fa fa 04 fa fa fa 06 fa
  0x0c047fffca10: fa fa fd fd fa fa fd fa fa fa fd fd fa fa 03 fa
  0x0c047fffca20: fa fa 06 fa fa fa fd fd fa fa fd fa fa fa 00 00
  0x0c047fffca30: fa fa 00 fa fa fa fd fa fa fa 00 fa fa fa 02 fa
  0x0c047fffca40: fa fa 00 00 fa fa 00 fa fa fa 06 fa fa fa 00 00
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
==51791==ABORTING

```

Thanks for your watching 

This autogeneration markdown is made by pySpider

Data : 2018-10-11 23:54:43 

Author: pwd 

Team : 360TeamSeri0us 

