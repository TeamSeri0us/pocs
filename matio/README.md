
## Description
matio is an C library for reading and writing MATLAB MAT files.
## Version

[1.5.13](https://sourceforge.net/projects/matio/files/matio/1.5.13/)

## Others

This bug is reported by fish@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have any question.

## Details

1.  There is a heap-buffer-overflow problem in function InflateVarName() in src/inflate.c:512.

### debug info 

```sh

fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./debug/debug/bin/matdump data/20190219-crash/inflate___heap-buffer-overflow
malloc(): memory corruption
Aborted (core dumped)

```


### gdb info 

```
#0  __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff73f0801 in __GI_abort () at abort.c:79
#2  0x00007ffff7439897 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7566b9a "%s\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff744090a in malloc_printerr (str=str@entry=0x7ffff7564e0e "malloc(): memory corruption") at malloc.c:5350
#4  0x00007ffff7444994 in _int_malloc (av=av@entry=0x7ffff779bc40 <main_arena>, bytes=bytes@entry=0x2d) at malloc.c:3738
#5  0x00007ffff74470fc in __GI___libc_malloc (bytes=0x2d) at malloc.c:3057
#6  0x00007ffff7b415c6 in strdup_vprintf (format=0x7ffff7bcf630 "InflateVarName: inflate returned %s", ap=0x7fffffffd8d0) at ../../src/io.c:63
#7  0x00007ffff7b419eb in mat_log (loglevel=0x2, format=0x7ffff7bcf630 "InflateVarName: inflate returned %s", ap=0x7fffffffd8d0) at ../../src/io.c:154
#8  0x00007ffff7b41de4 in Mat_Critical (format=0x7ffff7bcf630 "InflateVarName: inflate returned %s") at ../../src/io.c:343
#9  0x00007ffff7b435f9 in InflateVarName (mat=0x55555575c490, matvar=0x5555557674c0, buf=0x555555769470, N=0xffffffff) at ../../src/inflate.c:512
#10 0x00007ffff7b7a0f0 in ReadNextCell (mat=0x55555575c490, matvar=0x5555557674c0) at ../../src/mat5.c:1315
#11 0x00007ffff7b7a3c3 in ReadNextCell (mat=0x55555575c490, matvar=0x55555575d5f0) at ../../src/mat5.c:1337
#12 0x00007ffff7bc556d in Mat_VarReadNextInfo5 (mat=0x55555575c490) at ../../src/mat5.c:5693
#13 0x00007ffff7bccd4b in Mat_VarReadNextInfo (mat=0x55555575c490) at ../../src/mat.c:2181
#14 0x0000555555558874 in main (argc=0x2, argv=0x7fffffffde08) at ../../tools/matdump.c:934

```

2. There is a heap-buffer-overflow problem in function ReadNextCell() in src/mat5.c:1353.

### debug info 

```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./debug/debug/bin/matdump data/20190219-crash/inflate___heap-buffer-overflow-02 
corrupted size vs. prev_size
Aborted (core dumped)

```

### gdb info 

```
#0  __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff73f0801 in __GI_abort () at abort.c:79
#2  0x00007ffff7439897 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7566b9a "%s\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff744090a in malloc_printerr (str=str@entry=0x7ffff7564c9d "corrupted size vs. prev_size") at malloc.c:5350
#4  0x00007ffff744815f in _int_free (have_lock=0x0, p=<optimized out>, av=0x7ffff779bc40 <main_arena>) at malloc.c:4295
#5  __GI___libc_free (mem=<optimized out>) at malloc.c:3124
#6  0x00007ffff71a0351 in inflateEnd () from /lib/x86_64-linux-gnu/libz.so.1
#7  0x00007ffff7b7a52c in ReadNextCell (mat=0x55555575c490, matvar=0x55555575d5f0) at ../../src/mat5.c:1353
#8  0x00007ffff7bc556d in Mat_VarReadNextInfo5 (mat=0x55555575c490) at ../../src/mat5.c:5693
#9  0x00007ffff7bccd4b in Mat_VarReadNextInfo (mat=0x55555575c490) at ../../src/mat.c:2181
#10 0x0000555555558874 in main (argc=0x2, argv=0x7fffffffde08) at ../../tools/matdump.c:934


```

3. There is a stack-buffer-overflow problem in function InflateDimensions() in inflate.c:409.

### asan info 

```

fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./fast/fast/bin/matdump data/20190219-crash/inflate___stack-buffer-overflow 
=================================================================
==8243==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe0048ba80 at pc 0x00000046e6b2 bp 0x7ffe0048b840 sp 0x7ffe0048aff0
READ of size 1 at 0x7ffe0048ba80 thread T0
    #0 0x46e6b1 in __interceptor_memcpy.part.233 (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x46e6b1)
    #1 0x7fb74cfbe334 in inflate (/lib/x86_64-linux-gnu/libz.so.1+0xc334)
    #2 0x7fb74d1dd9c8 in InflateDimensions /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/inflate.c:409:15
    #3 0x7fb74d362a68 in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1274:30
    #4 0x7fb74d35d8c6 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5693:27
    #5 0x7fb74d373b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #6 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #7 0x7fb74c001b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #8 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

Address 0x7ffe0048ba80 is located in stack of thread T0 at offset 96 in frame
    #0 0x7fb74d36202f in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1197

  This frame has 2 object(s):
    [32, 96) 'uncomp_buf' <== Memory access at offset 96 overflows this variable
    [128, 152) 'buf'
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x46e6b1) in __interceptor_memcpy.part.233
Shadow bytes around the buggy address:
  0x100040089700: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100040089710: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x100040089720: 00 00 00 00 f2 f2 f2 f2 00 f3 f3 f3 00 00 00 00
  0x100040089730: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100040089740: 00 00 00 00 f1 f1 f1 f1 00 00 00 00 00 00 00 00
=>0x100040089750:[f2]f2 f2 f2 00 00 00 f3 f3 f3 f3 f3 00 00 00 00
  0x100040089760: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100040089770: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100040089780: 00 00 00 00 f1 f1 f1 f1 04 f2 04 f2 00 00 00 00
  0x100040089790: 00 00 00 00 f2 f2 f2 f2 00 00 00 f3 f3 f3 f3 f3
  0x1000400897a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==8243==ABORTING

```

### gdb info 

```
gef➤  bt
#0  0x00007ffff719e2fb in inflate () from /lib/x86_64-linux-gnu/libz.so.1
#1  0x00007ffff7b430fb in InflateDimensions (mat=0x55555575c490, matvar=0x55555575d5f0, buf=0x7fffffffdb50) at ../../src/inflate.c:409
#2  0x00007ffff7b79d9d in ReadNextCell (mat=0x55555575c490, matvar=0x55555575d5f0) at ../../src/mat5.c:1274
#3  0x3030303030303030 in ?? ()
#4  0x3030303030303030 in ?? ()
#5  0x3030303030303030 in ?? ()
#6  0x3030303030303030 in ?? ()
#7  0x3030303030303030 in ?? ()
#8  0x3030303030303030 in ?? ()
......
#649 0x3030303030303030 in ?? ()
#650 0x3030303030303030 in ?? ()
#651 0x3030303030303030 in ?? ()
Backtrace stopped: Cannot access memory at address 0x7ffffffff000


```

4. There is a stack-buffer-overflow in function Mat_VarReadNextInfo5() in  src/mat5.c:5757.

### asan info 

```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./fast/fast/bin/matdump data/20190219-crash/Mat_VarReadNextInfo5@mat5.c_5755-28___stack-buffer-overflow 
ASAN:DEADLYSIGNAL
=================================================================
==8332==ERROR: AddressSanitizer: SEGV on unknown address 0x00207fff8106 (pc 0x7fd9fa2a3168 bp 0x7ffef3062730 sp 0x7ffef3062540 T0)
==8332==The signal is caused by a READ memory access.
    #0 0x7fd9fa2a3167 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5757:30
    #1 0x7fd9fa2bab7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #2 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #3 0x7fd9f8f48b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #4 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5757:30 in Mat_VarReadNextInfo5
==8332==ABORTING

```

### gdb info 


```
   5753	                 else
   5754	                     i = len+(8-(len % 8));
   5755	                 bytesread+=fread(buf,1,i,(FILE*)mat->fp);
   5756	 
   5757	                 matvar->name = (char*)malloc(len+1);
		// len=0x10000, buf=0x00007fffffffdc00  →  0x0000050000000000, matvar=0x00007fffffffdbe0  →  [...]  →  0x0000000000000008
 → 5758	                 memcpy(matvar->name,buf,len);
   5759	                 matvar->name[len] = '\0';
   5760	             } else if ( ((buf[0] & 0x0000ffff) == MAT_T_INT8) &&
   5761	                         ((buf[0] & 0xffff0000) != 0x00) ) {
   5762	                 /* Name packed in the tag */
   5763	                 int len;
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "matdump", stopped, reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7bc585a → Name: Mat_VarReadNextInfo5(mat=0x55555575c490)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, Mat_VarReadNextInfo5 (mat=0x55555575c490) at ../../src/mat5.c:5758
5758	                memcpy(matvar->name,buf,len);
gef➤  p buf
$1 = {0x0, 0x500, 0x800, 0x100, 0x500, 0x100}
gef➤  p len
$2 = 0x10000

```


5. There is a stack-buffer-overflow problem function Mat_VarReadNextInfo5() in src/mat5.c:5767.

### asan info


```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./fast/fast/bin/matdump data/20190219-crash/Mat_VarReadNextInfo5@mat5.c_5767-17___stack-buffer-overflow 
=================================================================
==8393==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe6a451ef8 at pc 0x0000004b6791 bp 0x7ffe6a451e30 sp 0x7ffe6a4515e0
READ of size 63488 at 0x7ffe6a451ef8 thread T0
    #0 0x4b6790 in __asan_memcpy (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4b6790)
    #1 0x7fd1d8920fc5 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5767:17
    #2 0x7fd1d8938b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #3 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #4 0x7fd1d75c6b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

Address 0x7ffe6a451ef8 is located in stack of thread T0 at offset 184 in frame
    #0 0x7fd1d89206cf in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5564

  This frame has 4 object(s):
    [32, 36) 'data_type'
    [48, 52) 'nBytes'
    [64, 128) 'uncomp_buf'
    [160, 184) 'buf' <== Memory access at offset 184 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4b6790) in __asan_memcpy
Shadow bytes around the buggy address:
  0x10004d482380: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d482390: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d4823a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d4823b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d4823c0: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 04 f2 04 f2
=>0x10004d4823d0: 00 00 00 00 00 00 00 00 f2 f2 f2 f2 00 00 00[f3]
  0x10004d4823e0: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d4823f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d482400: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x10004d482410: 00 04 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004d482420: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==8393==ABORTING


```

### gdb info 

```
   5762	                 /* Name packed in the tag */
   5763	                 int len;
   5764	 
   5765	                 len = (buf[0] & 0xffff0000) >> 16;
   5766	                 matvar->name = (char*)malloc(len+1);
		// len=0xf800, buf=0x00007fffffffdc00  →  InflateData: inflate returned data error
InflateSkip: inflate returned data error
InflateSkip: inflate returned data error
InflateSkip: inflate returned data error
      Name: teststructnest
      Rank: 2
Class Type: Structure
Fields[2] {
          Name: two
          Rank: 2
    Class Type: Structure
    Fields[1] {
      Name: three
      Rank: 2
Dimensions: 1 x 8
Class Type: Character Array (complex)
 Data Type: Unicode UTF-16 Encoded Character Data
    }
}
ASAN:DEADLYSIGNAL
=================================================================
==3243==ERROR: AddressSanitizer: SEGV on unknown address 0x000011111101 (pc 0x000000420e05 bp 0x7ffcc8da78b0 sp 0x7ffcc8da7860 T0)
==3243==The signal is caused by a WRITE memory access.
    #0 0x420e04 in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04)
    #1 0x4cbd93 in __interceptor_free.localalias.0 (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4cbd93)
    #2 0x7f1f531ecd62 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1473:17
    #3 0x7f1f531ed511 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1384:25
    #4 0x7f1f531ed511 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1384:25
    #5 0x509eb5 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:936:17
    #6 0x7f1f51e7cb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #7 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04) in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType)
==3243==ABORTING
0x05000000f8000001, matvar=0x00007fffffffdbe0  →  [...]  →  0x0000000000000000
 → 5767	                 memcpy(matvar->name,buf+1,len);
   5768	                 matvar->name[len] = '\0';
   5769	             }
   5770	             if ( matvar->class_type == MAT_C_STRUCT )
   5771	                 (void)ReadNextStructField(mat,matvar);
   5772	             else if ( matvar->class_type == MAT_C_CELL )
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "matdump", stopped, reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7bc58d2 → Name: Mat_VarReadNextInfo5(mat=0x55555575c490)
[#1] 0x7ffff7bccd4b → Name: Mat_VarReadNextInfo(mat=0x55555575c490)
[#2] 0x555555558874 → Name: main(argc=0x2, argv=0x7fffffffdde8)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, Mat_VarReadNextInfo5 (mat=0x55555575c490) at ../../src/mat5.c:5767
5767	                memcpy(matvar->name,buf+1,len);
gef➤  p buf
$1 = {0xf8000001, 0x5000000, 0x1, 0x0, 0x4b8a32, 0xf3d28b19}
gef➤  p len
$2 = 0xf800

```

6. There is an  out-of-bound read problem in function Mat_VarFree()  in mat.c:1473.


### asan info 

```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ ./fast/fast/bin/matdump data/20190219-crash/Mat_VarFree@mat.c_1473-17___out-of-bounds-read 
InflateArrayFlags: inflate returned data error
InflateDimensions: inflate returned data error
InflateVarNameTag: inflate returned data error
InflateVarTag: inflate returned data error
InflateSkip: inflate returned data error
InflateVarTag: inflate returned data error
fields[2], Uncompressed type not MAT_T_MATRIX
      Name: teststruct
      Rank: 2
Class Type: Structure
Fields[3] {
      Name: stringfield
      Rank: 2
Dimensions: 1 x 26
Class Type: Character Array (complex)
 Data Type: Unicode UTF-8 Encoded Character Data
          Name: doublefield
          Rank: 0
}
ASAN:DEADLYSIGNAL
=================================================================
==8418==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000420e05 bp 0x7ffef4ebdbe0 sp 0x7ffef4ebdb90 T0)
==8418==The signal is caused by a READ memory access.
==8418==Hint: address points to the zero page.
    #0 0x420e04 in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04)
    #1 0x4cbd93 in __interceptor_free.localalias.0 (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4cbd93)
    #2 0x7f376fdc4d62 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1473:17
    #3 0x7f376fdc5511 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1384:25
    #4 0x509eb5 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:936:17
    #5 0x7f376ea54b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04) in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType)
==8418==ABORTING

```

7. There is an out-of-bound write problem in function Mat_VarFree() in src/mat.c:1473.


### asan info 

```
InflateData: inflate returned data error
InflateSkip: inflate returned data error
InflateSkip: inflate returned data error
InflateSkip: inflate returned data error
      Name: teststructnest
      Rank: 2
Class Type: Structure
Fields[2] {
          Name: two
          Rank: 2
    Class Type: Structure
    Fields[1] {
      Name: three
      Rank: 2
Dimensions: 1 x 8
Class Type: Character Array (complex)
 Data Type: Unicode UTF-16 Encoded Character Data
    }
}
ASAN:DEADLYSIGNAL
=================================================================
==3243==ERROR: AddressSanitizer: SEGV on unknown address 0x000011111101 (pc 0x000000420e05 bp 0x7ffcc8da78b0 sp 0x7ffcc8da7860 T0)
==3243==The signal is caused by a WRITE memory access.
    #0 0x420e04 in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04)
    #1 0x4cbd93 in __interceptor_free.localalias.0 (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4cbd93)
    #2 0x7f1f531ecd62 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1473:17
    #3 0x7f1f531ed511 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1384:25
    #4 0x7f1f531ed511 in Mat_VarFree /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1384:25
    #5 0x509eb5 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:936:17
    #6 0x7f1f51e7cb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #7 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x420e04) in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType)
==3243==ABORTING

```


8. There is a stack-buffer-overflow  problem in function ReadNextCell() in src/mat5.c:1293.

### asan info 

```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ fast/fast/bin/matdump data/vuln/matdump-14-vuln/ReadNextCell@mat5.c_1293-49___stack-buffer-overflow
InflateDimensions: inflate returned data error
=================================================================
==4094==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe432e9e60 at pc 0x7f6b790ff08a bp 0x7ffe432e9df0 sp 0x7ffe432e9de8
READ of size 4 at 0x7ffe432e9e60 thread T0
    #0 0x7f6b790ff089 in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1293:49
    #1 0x7f6b790f78c6 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5693:27
    #2 0x7f6b7910db7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #3 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #4 0x7f6b77d9bb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

Address 0x7ffe432e9e60 is located in stack of thread T0 at offset 96 in frame
    #0 0x7f6b790fc02f in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1197

  This frame has 2 object(s):
    [32, 96) 'uncomp_buf' <== Memory access at offset 96 overflows this variable
    [128, 152) 'buf'
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1293:49 in ReadNextCell
Shadow bytes around the buggy address:
  0x100048655370: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100048655380: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100048655390: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000486553a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000486553b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x1000486553c0: f1 f1 f1 f1 00 00 00 00 00 00 00 00[f2]f2 f2 f2
  0x1000486553d0: 00 00 00 f3 f3 f3 f3 f3 00 00 00 00 00 00 00 00
  0x1000486553e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000486553f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100048655400: f1 f1 f1 f1 04 f2 04 f2 00 00 00 00 00 00 00 00
  0x100048655410: f2 f2 f2 f2 00 00 00 f3 f3 f3 f3 f3 00 00 00 00
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
==4094==ABORTING

```

9. There is a stack-buffer-overflow problem in function ReadNextCell() in src/mat5.c:1323.


### asan info 

```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ fast/fast/bin/matdump data/vuln/matdump-14-vuln/ReadNextCell@mat5.c_1323-25___stack-buffer-overflow 
=================================================================
==4103==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff98e1d9c0 at pc 0x0000004b6791 bp 0x7fff98e1d950 sp 0x7fff98e1d100
READ of size 2048 at 0x7fff98e1d9c0 thread T0
    #0 0x4b6790 in __asan_memcpy (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4b6790)
    #1 0x7f9970ce52c5 in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1323:25
    #2 0x7f9970cdf8c6 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5693:27
    #3 0x7f9970cf5b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #4 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #5 0x7f996f983b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

Address 0x7fff98e1d9c0 is located in stack of thread T0 at offset 96 in frame
    #0 0x7f9970ce402f in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1197

  This frame has 2 object(s):
    [32, 96) 'uncomp_buf'
    [128, 152) 'buf' <== Memory access at offset 96 partially underflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4b6790) in __asan_memcpy
Shadow bytes around the buggy address:
  0x1000731bbae0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbaf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbb00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbb10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbb20: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
=>0x1000731bbb30: 00 00 00 00 00 00 00 00[f2]f2 f2 f2 00 00 00 f3
  0x1000731bbb40: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbb50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1000731bbb60: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x1000731bbb70: 04 f2 04 f2 00 00 00 00 00 00 00 00 f2 f2 f2 f2
  0x1000731bbb80: 00 00 00 f3 f3 f3 f3 f3 00 00 00 00 00 00 00 00
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
==4103==ABORTING

```


10. There is an out-of-bound write problem in function ReadNextFunctionHandle() in  mat5.c:1837.

### asan info
```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ fast/fast/bin/matdump data/20190219-crash/ReadNextFunctionHandle@mat5.c_1837-26___heap-buffer-overflow 
=================================================================
==4304==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000efd0 at pc 0x7fa46119fcf7 bp 0x7fffb2a675d0 sp 0x7fffb2a675c8
WRITE of size 8 at 0x60200000efd0 thread T0
    #0 0x7fa46119fcf6 in ReadNextFunctionHandle /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1837:26
    #1 0x7fa46119fcf6 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5775
    #2 0x7fa4611b5b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #3 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #4 0x7fa45fe43b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

0x60200000efd1 is located 0 bytes to the right of 1-byte region [0x60200000efd0,0x60200000efd1)
allocated by thread T0 here:
    #0 0x4cbf70 in malloc (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x4cbf70)
    #1 0x7fa46119e5f1 in ReadNextFunctionHandle /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1830:20
    #2 0x7fa46119e5f1 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5775
    #3 0x7fa4611b5b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #4 0x7fa45fe43b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1837:26 in ReadNextFunctionHandle
Shadow bytes around the buggy address:
  0x0c047fff9da0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9db0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9dc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9dd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9de0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c047fff9df0: fa fa fa fa fa fa fa fa fa fa[01]fa fa fa 00 fa
  0x0c047fff9e00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9e10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9e20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9e30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9e40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==4304==ABORTING
```


11. There is a  stack-buffer-overflow problem in function ReadNextStructField() in mat5.c:1629.


### asan info 

```
...
=================================================================
==4485==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffd0bbd3240 at pc 0x7f13e062ff3e bp 0x7ffd0bbd31d0 sp 0x7ffd0bbd31c8
READ of size 4 at 0x7ffd0bbd3240 thread T0
    #0 0x7f13e062ff3d in ReadNextStructField /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1629:50
    #1 0x7f13e062b892 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5691:27
    #2 0x7f13e0641b7c in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #3 0x509e44 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:934:31
    #4 0x7f13df2cfb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

Address 0x7ffd0bbd3240 is located in stack of thread T0 at offset 96 in frame
    #0 0x7f13e062c16f in ReadNextStructField /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1482

  This frame has 2 object(s):
    [32, 96) 'uncomp_buf' <== Memory access at offset 96 overflows this variable
    [128, 152) 'buf'
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1629:50 in ReadNextStructField
Shadow bytes around the buggy address:
  0x1000217725f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772600: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772610: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772620: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772630: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
=>0x100021772640: 00 00 00 00 00 00 00 00[f2]f2 f2 f2 00 00 00 f3
  0x100021772650: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772660: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100021772670: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x100021772680: 04 f2 04 f2 00 00 00 00 00 00 00 00 f2 f2 f2 f2
  0x100021772690: 00 00 00 f3 f3 f3 f3 f3 00 00 00 00 00 00 00 00
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
==4485==ABORTING

```


### gdb info 

```
──────────────────────────────────────────────────────────────────────────────────────────────────────────[ source:../../src/mat5.c+1629 ]────
   1624	                     if ( mat->byteswap ) {
   1625	                         for ( j = 0; j < fields[i]->rank; j++ )
   1626	                             fields[i]->dims[j] = Mat_uint32Swap(uncomp_buf+2+j);
   1627	                     } else {
   1628	                         for ( j = 0; j < fields[i]->rank; j++ )
		// uncomp_buf=0x00007fffffffdb80  →  0x3010000800000005, j=0x51e, fields=0x00007fffffffdb60  →  [...]  →  0x0000000000000800
 → 1629	                             fields[i]->dims[j] = uncomp_buf[2+j];
   1630	                     }
   1631	                     if ( fields[i]->rank % 2 != 0 )
   1632	                         nbytes -= 4;
   1633	                 }
   1634	                 bytesread += InflateVarNameTag(mat,matvar,uncomp_buf);
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "matdump", stopped, reason: SIGSEGV
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7b7b6a4 → Name: ReadNextStructField(mat=0x55555575c490, matvar=0x55555575d610)
[#1] 0x7ffff7bc5549 → Name: Mat_VarReadNextInfo5(mat=0x55555575c490)
[#2] 0x7ffff7bccd4b → Name: Mat_VarReadNextInfo(mat=0x55555575c490)
[#3] 0x555555558874 → Name: main(argc=0x2, argv=0x7fffffffde38)
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
0x00007ffff7b7b6a4 in ReadNextStructField (mat=0x55555575c490, matvar=0x55555575d610) at ../../src/mat5.c:1629
1629	                            fields[i]->dims[j] = uncomp_buf[2+j];
gef➤  p uncomp_buf
$5 = {0x5, 0x30100008, 0x6000000, 0x8000000, 0x6000000, 0x59260800, 0x21, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0}
gef➤  p j
$6 = 0x51e
gef➤  p uncomp_buf[2+j]
Cannot access memory at address 0x7ffffffff000

```

12. There is a global buffer-overflow problem in function Mat_VarPrint() in mat.c:1835.

### asan info
```
fish@ubuntu:~/Desktop/dumb/text/matio-1.5.13$ fast/fast/bin/matdump data/20190219-crash/Mat_VarPrint@mat.c_1835-36___global-buffer-overflow
ReadCompressedCharData: 23 is not a supported data type for character data
InflateSkip: inflate returned data error
InflateSkip: inflate returned data error
      Name: teststructnest
      Rank: 2
Class Type: Structure
Fields[2] {
          Name: two
          Rank: 2
    Class Type: Structure
    Fields[1] {
      Name: three
      Rank: 2
Dimensions: 1 x 8
Class Type: Character Array (logical)
=================================================================
==4555==ERROR: AddressSanitizer: global-buffer-overflow on address 0x7f4ef6fbc798 at pc 0x7f4ef6daa0ad bp 0x7ffd52317360 sp 0x7ffd52317358
READ of size 8 at 0x7f4ef6fbc798 thread T0
    #0 0x7f4ef6daa0ac in Mat_VarPrint /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1835:36
    #1 0x50b63b in print_default /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:758:13
    #2 0x50c743 in print_default /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:789:21
    #3 0x50c743 in print_default /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:789:21
    #4 0x509ead in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:935:17
    #5 0x7f4ef5a2bb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

0x7f4ef6fbc798 is located 0 bytes to the right of global variable 'Mat_VarPrint.data_type_desc' defined in '../../src/mat.c' (0x7f4ef6fbc6e0) of size 184
SUMMARY: AddressSanitizer: global-buffer-overflow /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:1835:36 in Mat_VarPrint
Shadow bytes around the buggy address:
  0x0fea5edef8a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef8b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef8c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef8d0: 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9 00 00 00 00
  0x0fea5edef8e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0fea5edef8f0: 00 00 00[f9]f9 f9 f9 f9 00 00 00 00 00 00 00 00
  0x0fea5edef900: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef910: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef920: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef930: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fea5edef940: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==4555==ABORTING
```

### gdb info

```
  1830	            "64-bit, signed integer","64-bit, unsigned integer", "Matlab Array",
   1831	            "Compressed Data","Unicode UTF-8 Encoded Character Data",
   1832	            "Unicode UTF-16 Encoded Character Data",
   1833	            "Unicode UTF-32 Encoded Character Data","","String","Cell Array",
   1834	            "Structure"};
		// data_type_desc=0x00007fffffffdb00  →  [...]  →  0x006e776f6e6b6e55 ("Unknown"?), matvar=0x00007fffffffd9a8  →  [...]  →  0x0000000000001717
 → 1835	         printf(" Data Type: %s\n", data_type_desc[matvar->data_type]);
   1836	     }
   1837	 
   1838	     if ( MAT_C_STRUCT == matvar->class_type ) {
   1839	         matvar_t **fields = (matvar_t **)matvar->data;
   1840	         size_t nfields = matvar->internal->num_fields;
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "matdump", stopped, reason: BREAKPOINT
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7bcbeb4 → Name: Mat_VarPrint(matvar=0x555555769310, printdata=0x0)
[#1] 0x55555555806c → Name: print_default(matvar=0x555555769310)
[#2] 0x55555555824d → Name: print_default(matvar=0x5555557674a0)
[#3] 0x55555555824d → Name: print_default(matvar=0x55555575d610)
[#4] 0x55555555885c → Name: main(argc=0x2, argv=0x7fffffffde38)
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Breakpoint 1, Mat_VarPrint (matvar=0x555555769310, printdata=0x0) at ../../src/mat.c:1835
1835	        printf(" Data Type: %s\n", data_type_desc[matvar->data_type]);
gef➤  p matvar->data_type
$1 = MAT_T_ARRAY        // data_type_desc = 23, off-by-one error.
gef➤  p data_type_desc[matvar->data_type]
$2 = 0x97bcb90ceebfdd00 <error: Cannot access memory at address 0x97bcb90ceebfdd00>

```

13. There is an out-of-bound read problem in function ReadNextCell() in src/mat5.c:1342.


### asan info 

```
2 3 
3 4 
InflateData: inflate returned data error
InflateSkip: inflate returned data error
ASAN:DEADLYSIGNAL
=================================================================
==4973==ERROR: AddressSanitizer: SEGV on unknown address 0x000d0d8dcdf5 (pc 0x7ff7dd6ef82a bp 0x7fffb143f490 sp 0x7fffb143f2a0 T0)
==4973==The signal is caused by a READ memory access.
    #0 0x7ff7dd6ef829 in ReadNextCell /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1342:70
    #1 0x7ff7dd6e98c6 in Mat_VarReadNextInfo5 /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:5693:27
    #2 0x7ff7dd70313f in Mat_VarReadNextInfo /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2181:22
    #3 0x7ff7dd70313f in Mat_VarReadNext /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat.c:2324
    #4 0x509db6 in main /home/fish/Desktop/dumb/text/matio-1.5.13/fast/tools/../../tools/matdump.c:929:31
    #5 0x7ff7dc38db96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #6 0x41c999 in _start (/home/fish/Desktop/dumb/text/matio-1.5.13/fast/fast/bin/matdump+0x41c999)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/dumb/text/matio-1.5.13/fast/src/../../src/mat5.c:1342:70 in ReadNextCell
==4973==ABORTING

```


### gdb info 

```
gef➤  bt
#0  __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff73f0801 in __GI_abort () at abort.c:79
#2  0x00007ffff7439897 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7566b9a "%s\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff744090a in malloc_printerr (str=str@entry=0x7ffff7564e0e "malloc(): memory corruption") at malloc.c:5350
#4  0x00007ffff7444994 in _int_malloc (av=av@entry=0x7ffff779bc40 <main_arena>, bytes=bytes@entry=0x2a) at malloc.c:3738
#5  0x00007ffff74470fc in __GI___libc_malloc (bytes=0x2a) at malloc.c:3057
#6  0x00007ffff7b415c6 in strdup_vprintf (format=0x7ffff7bcf6b0 "InflateData: inflate returned %s", ap=0x7fffffffd4b0) at ../../src/io.c:63
#7  0x00007ffff7b419eb in mat_log (loglevel=0x2, format=0x7ffff7bcf6b0 "InflateData: inflate returned %s", ap=0x7fffffffd4b0) at ../../src/io.c:154
#8  0x00007ffff7b41de4 in Mat_Critical (format=0x7ffff7bcf6b0 "InflateData: inflate returned %s") at ../../src/io.c:343
#9  0x00007ffff7b43cbf in InflateData (mat=0x55555575c490, z=0x55555575f440, buf=0x5555557610c0, nBytes=0x145) at ../../src/inflate.c:670
#10 0x00007ffff7b638f4 in ReadCompressedCharData (mat=0x55555575c490, z=0x55555575f440, data=0x5555557610c0 "hello", data_type=MAT_T_UTF8, len=0x145) at ../../src/read_data.c:1363
#11 0x00007ffff7b81235 in Read5 (mat=0x55555575c490, matvar=0x55555575f3b0) at ../../src/mat5.c:3303
#12 0x00007ffff7b7a403 in ReadNextCell (mat=0x55555575c490, matvar=0x55555575d600) at ../../src/mat5.c:1341
#13 0x00007ffff7bc556d in Mat_VarReadNextInfo5 (mat=0x55555575c490) at ../../src/mat5.c:5693
#14 0x00007ffff7bccd4b in Mat_VarReadNextInfo (mat=0x55555575c490) at ../../src/mat.c:2181
#15 0x00007ffff7bcd120 in Mat_VarReadNext (mat=0x55555575c490) at ../../src/mat.c:2324
#16 0x000055555555883d in main (argc=0x3, argv=0x7fffffffde38) at ../../tools/matdump.c:929

```
