
# Description
MuPDF is a lightweight PDF, XPS, and E-book viewer. MuPDF consists of a software library, command line tools, and viewers for various platforms.
# version
1.14.0

# others
## @_@

this bug is reported by fish@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detail


#

## target
```
mupdf
```
## details
```

1. fish@ubuntu:~/Desktop/2018-10-10/pdf/mupdf$ ./afl/bin/mupdf-gl out-of-bound-read-poc-2.svg
ASAN:DEADLYSIGNAL
=================================================================
==69945==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f8c571827d9 bp 0x7ffea3fa0d50 sp 0x7ffea3fa04b0 T0)
==69945==The signal is caused by a READ memory access.
==69945==Hint: address points to the zero page.
    #0 0x7f8c571827d8  (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x5a7d8)
    #1 0x55b5924dece2  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x18dce2)
    #2 0x55b59295ec9d  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60dc9d)
    #3 0x55b592961123  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x610123)
    #4 0x55b5925a324e  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x25224e)
    #5 0x55b5927f70f9  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x4a60f9)
    #6 0x55b59252ff5c  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x1def5c)
    #7 0x55b5924f646f  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x1a546f)
    #8 0x7f8c561ebb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #9 0x55b5924fe979  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x1ad979)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x5a7d8) 
==69945==ABORTING

fish@ubuntu:~/Desktop/2018-10-10/pdf/mupdf$ gdb -q --args ./debug/bin/mupdf-gl out-of-bound-read-poc-2.svg 

198	../sysdeps/x86_64/multiarch/strcmp-sse42.S: No such file or directory.
gef➤  bt
#0  __strncmp_sse42 () at ../sysdeps/x86_64/multiarch/strcmp-sse42.S:198
#1  0x00005555556882e0 in svg_run_image (ctx=0x555557f89b10, dev=0x55555802f130, doc=0x555557f89bb0, root=0x555557fd4d40, inherit_state=0x7fffffffd960) at source/svg/svg-run.c:1095
#2  0x0000555555688809 in svg_run_element (ctx=0x555557f89b10, dev=0x55555802f130, doc=0x555557f89bb0, root=0x555557fd4d40, state=0x7fffffffd960) at source/svg/svg-run.c:1166
#3  0x00005555556879d4 in svg_run_svg (ctx=0x555557f89b10, dev=0x55555802f130, doc=0x555557f89bb0, root=0x555557fd4738, inherit_state=0x7fffffffdaa0) at source/svg/svg-run.c:1004
#4  0x0000555555688ca7 in svg_run_document (ctx=0x555557f89b10, doc=0x555557f89bb0, root=0x555557fd4738, dev=0x55555802f130, ctm=...) at source/svg/svg-run.c:1265
#5  0x00005555556833c9 in svg_run_page (ctx=0x555557f89b10, page_=0x555557f2af70, dev=0x55555802f130, ctm=..., cookie=0x0) at source/svg/svg-doc.c:42
#6  0x00005555555c94be in fz_run_page_contents (ctx=0x555557f89b10, page=0x555557f2af70, dev=0x55555802f130, transform=..., cookie=0x0) at source/fitz/document.c:393
#7  0x0000555555637f7e in fz_new_stext_page_from_page (ctx=0x555557f89b10, page=0x555557f2af70, options=0x0) at source/fitz/util.c:324
#8  0x00005555555b3c8f in load_page () at platform/gl/gl-main.c:468
#9  0x00005555555b7799 in main (argc=0x2, argv=0x7fffffffde68) at platform/gl/gl-main.c:1578


 char *href_att = fz_xml_att(root, "xlink:href");

 if (!strncmp(href_att, jpeg_uri, strlen(jpeg_uri)))
                data = href_att + strlen(jpeg_uri);


The value of the href_att pointer is null, which triggered the crash. More details about the svg format can be found at [here](https://www.w3.org/TR/SVG2/linking.html#XLinkRefAttrs).

2. fish@ubuntu:~/Desktop/2018-10-10/pdf/mupdf$ ./afl/bin/mupdf-gl stack-overflow-poc-1.svg
ASAN:DEADLYSIGNAL
=================================================================
==70456==ERROR: AddressSanitizer: stack-overflow on address 0x7ffcd7f05ea8 (pc 0x7f27dac74e6f bp 0x7ffcd7f06710 sp 0x7ffcd7f05e70 T0)
    #0 0x7f27dac74e6e  (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x59e6e)
    #1 0x562cafbd1593  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x742593)
    #2 0x562cafa9b26c  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60c26c)
    #3 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #4 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    ......
      #245 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #246 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #247 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #248 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #249 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)
    #250 0x562cafa9bdcc  (/home/fish/Desktop/2018-10-10/pdf/mupdf/afl/bin/mupdf-gl+0x60cdcc)

SUMMARY: AddressSanitizer: stack-overflow (/usr/lib/x86_64-linux-gnu/libasan.so.4+0x59e6e) 
==70456==ABORTING

   193	 char *fz_xml_att(fz_xml *item, const char *name)
 →  194	 {
    195	 	struct attribute *att;
    196	 	if (!item)
    197	 		return NULL;
    198	 	for (att = item->atts; att; att = att->next)
    199	 		if (!strcmp(att->name, name))
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "mupdf-gl", stopped, reason: SIGSEGV
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[!] Cannot access memory at address 0x7fffff7fefe8
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
0x00005555556d5aa8 in fz_xml_att (item=<error reading variable: Cannot access memory at address 0x7fffff7fefe8>, name=<error reading variable: Cannot access memory at address 0x7fffff7fefe0>) at source/fitz/xml.c:194
194	{
gef➤  p item
Cannot access memory at address 0x7fffff7fefe8
gef➤  bt 10
#0  0x00005555556d5aa8 in fz_xml_att (item=<error reading variable: Cannot access memory at address 0x7fffff7fefe8>, name=<error reading variable: Cannot access memory at address 0x7fffff7fefe0>) at source/fitz/xml.c:194
#1  0x0000555555686fdb in svg_parse_viewbox (ctx=0x555557f89b10, doc=0x555557f89bb0, node=0x555557fd42d8, state=0x7fffff7ff110) at source/svg/svg-run.c:823
#2  0x0000555555687bd1 in svg_run_use_symbol (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, use=0x555557fd42d8, symbol=0x555557fd4238, inherit_state=0x7fffff7ff2c0) at source/svg/svg-run.c:1026
#3  0x0000555555687f0c in svg_run_use (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, root=0x555557fd42d8, inherit_state=0x7fffff7ff460) at source/svg/svg-run.c:1057
#4  0x0000555555688637 in svg_run_element (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, root=0x555557fd42d8, state=0x7fffff7ff460) at source/svg/svg-run.c:1148
#5  0x0000555555687c3b in svg_run_use_symbol (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, use=0x555557fd42d8, symbol=0x555557fd4238, inherit_state=0x7fffff7ff610) at source/svg/svg-run.c:1030
#6  0x0000555555687f0c in svg_run_use (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, root=0x555557fd42d8, inherit_state=0x7fffff7ff7b0) at source/svg/svg-run.c:1057
#7  0x0000555555688637 in svg_run_element (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, root=0x555557fd42d8, state=0x7fffff7ff7b0) at source/svg/svg-run.c:1148
#8  0x0000555555687c3b in svg_run_use_symbol (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, use=0x555557fd42d8, symbol=0x555557fd4238, inherit_state=0x7fffff7ff960) at source/svg/svg-run.c:1030
#9  0x0000555555687f0c in svg_run_use (ctx=0x555557f89b10, dev=0x55555802f140, doc=0x555557f89bb0, root=0x555557fd42d8, inherit_state=0x7fffff7ffb00) at source/svg/svg-run.c:1057
(More stack frames follow...)




```


Thanks for your watching 

This markdown is automatically  made by pySpider

Date : 2018-12-3 17:00:00 

Author: fish 

Team : 360TeamSeri0us 

