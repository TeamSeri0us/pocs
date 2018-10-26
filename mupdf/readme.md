
# Description
MuPDF is a lightweight PDF, XPS, and E-book viewer. MuPDF consists of a software library, command line tools, and viewers for various platforms.
# version
1.14.0

# others
## @_@

this bug is reported by fish@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detail


# [vuln/fz_run_t3_glyph@font.c-1398___out-of-bounds-read](#description)

## target
```
mutool draw -F svg -o out.svg $POC
```
## gdb info
```
#0  0x00005555555f9857 in fz_run_t3_glyph (ctx=0x555557b9d260, font=0x555557beea20, gid=0x5039, trm=..., dev=0x555557bca970) at source/fitz/font.c:1397
#1  0x0000555555648987 in svg_dev_text_span_as_paths_defs (ctx=0x555557b9d260, dev=0x555557bca970, span=0x555557bffa90, ctm=...) at source/fitz/svg-device.c:496
#2  0x0000555555649779 in svg_dev_fill_text (ctx=0x555557b9d260, dev=0x555557bca970, text=0x555557bffa70, ctm=..., colorspace=0x555557bacf70, color=0x7fffffffd210, alpha=1, color_params=0x7fffffffd15c) at source/fitz/svg-device.c:685
#3  0x00005555555c9d4f in fz_fill_text (ctx=0x555557b9d260, dev=0x555557bca970, text=0x555557bffa70, ctm=..., colorspace=0x555557bacf70, color=0x7fffffffd210, alpha=1, color_params=0x7fffffffd15c) at source/fitz/device.c:199
#4  0x00005555556087c6 in fz_run_display_list (ctx=0x555557b9d260, list=0x555557bc9780, dev=0x555557bca970, top_ctm=..., scissor=..., cookie=0x7fffffffd900) at source/fitz/list-device.c:1717
#5  0x0000555555595aab in dodrawpage (ctx=0x555557b9d260, page=0x555557bc8b00, list=0x555557bc9780, pagenum=0x1, cookie=0x7fffffffd900, start=0x0, interptime=0x0, filename=0x7fffffffe253 "222.pdf", bg=0x0, seps=0x0) at source/tools/mudraw.c:688
#6  0x0000555555597996 in drawpage (ctx=0x555557b9d260, doc=0x555557bb67f0, pagenum=0x1) at source/tools/mudraw.c:1176
#7  0x0000555555597b0e in drawrange (ctx=0x555557b9d260, doc=0x555557bb67f0, range=0x5555558de254 "") at source/tools/mudraw.c:1205
#8  0x0000555555599c3b in mudraw_main (argc=0x6, argv=0x7fffffffde50) at source/tools/mudraw.c:1922
#9  0x0000555555593972 in main (argc=0x7, argv=0x7fffffffde48) at source/tools/mutool.c:132
#10 0x00007ffff6fd0b97 in __libc_start_main (main=0x5555555936cc <main>, argc=0x7, argv=0x7fffffffde48, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffde38) at ../csu/libc-start.c:310
#11 0x000055555559357a in _start ()


```
## asan report
```


fish@ubuntu:~/Desktop/2018-10-10/mupdf$ sanitize/mutool draw -F svg -o /tmp/out.svg 222.pdf 
warning: ignoring zlib error: incorrect data check
page 222.pdf 1warning: ... repeated 2 times ...
warning: freetype load glyph (gid 20537): invalid argument
ASAN:DEADLYSIGNAL
=================================================================
==11234==ERROR: AddressSanitizer: SEGV on unknown address 0x0000000281c8 (pc 0x55f67eb20400 bp 0x7ffca69a8bb0 sp 0x7ffca69a8af0 T0)
==11234==The signal is caused by a READ memory access.
    #0 0x55f67eb203ff in fz_run_t3_glyph source/fitz/font.c:1398
    #1 0x55f67ebf4cc8 in svg_dev_text_span_as_paths_defs source/fitz/svg-device.c:495
    #2 0x55f67ebf6bf1 in svg_dev_fill_text source/fitz/svg-device.c:684
    #3 0x55f67eaa9a35 in fz_fill_text source/fitz/device.c:199
    #4 0x55f67eb4a806 in fz_run_display_list source/fitz/list-device.c:1718
    #5 0x55f67ea3476e in dodrawpage source/tools/mudraw.c:690
    #6 0x55f67ea38876 in drawpage source/tools/mudraw.c:1178
    #7 0x55f67ea38dc5 in drawrange source/tools/mudraw.c:1207
    #8 0x55f67ea3cf15 in mudraw_main source/tools/mudraw.c:1924
    #9 0x55f67ea2f9b5 in main source/tools/mutool.c:132
    #10 0x7fec6adc1b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #11 0x55f67ea2f1b9 in _start (/home/fish/Desktop/2018-10-10/mupdf/sanitize/mutool+0x1491b9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV source/fitz/font.c:1398 in fz_run_t3_glyph
==11234==ABORTING

```



Thanks for your watching 

This markdown is automatically  made by pySpider

Data : 2018-10-26 16:12:10 

Author: fish 

Team : 360TeamSeri0us 

