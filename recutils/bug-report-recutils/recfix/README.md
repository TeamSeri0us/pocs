
# Description
None
# version
None

# others
## @_@
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.

# Detial


# [vuln/rec_fex_parse_str_simple@rec-fex.c:618-44___heap-buffer-overflow](#description)
## target
```
recfix --auto @@
```
## gdb info
```c
In file: /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-fex.c
   613               elem->function_data = NULL;
   614               elem->rewrite_to = NULL;
   615               elem->str = strdup (elem_str);
   616               elem->min = -1;
   617               elem->max = -1;
 ► 618               new->elems[new->num_elems++] = elem;
   619             }
   620           else
   621             {
   622               res = false;
   623               break;

```
## asan report
```
=================================================================
==30571==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d000007690 at pc 0x7fa6db09e374 bp 0x7fff2a396010 sp 0x7fff2a396008
WRITE of size 8 at 0x61d000007690 thread T0
    #0 0x7fa6db09e373 in rec_fex_parse_str_simple /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-fex.c:618:44
    #1 0x7fa6db09d026 in rec_fex_new /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-fex.c:112:20
    #2 0x7fa6db077d3c in rec_int_check_descriptor /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:1007:21
    #3 0x7fa6db077d3c in rec_int_check_rset /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:156
    #4 0x7fa6db07530b in rec_int_check_db /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:112:19
    #5 0x5181bf in recfix_check_database /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:344:10
    #6 0x5181bf in recfix_do_auto /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:521
    #7 0x5181bf in main /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:558
    #8 0x7fa6d9edab96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #9 0x41c3e9 in _start (/home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/installed-asan/bin/recfix+0x41c3e9)

0x61d000007690 is located 0 bytes to the right of 2064-byte region [0x61d000006e80,0x61d000007690)
allocated by thread T0 here:
    #0 0x4dc2a0 in __interceptor_malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fa6db09c55e in rec_fex_new /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-fex.c:83:9
    #2 0x7fa6db077d3c in rec_int_check_descriptor /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:1007:21
    #3 0x7fa6db077d3c in rec_int_check_rset /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:156
    #4 0x7fa6db07530b in rec_int_check_db /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:112:19

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-fex.c:618:44 in rec_fex_parse_str_simple
Shadow bytes around the buggy address:
  0x0c3a7fff8e80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8e90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8ea0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8eb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fff8ec0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fff8ed0: 00 00[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8ee0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8ef0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8f00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8f10: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8f20: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
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
==30571==ABORTING

```


# [vuln/rec_type_check_enum@rec-types.c:1431-23___stack-buffer-overflow](#description)
## target
```
recfix --auto @@
```
## gdb info

```c
In file: /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-types.c
   1426                    || rec_letter_p (*p)
   1427                    || rec_digit_p (*p)
   1428                    || (*p == '_')
   1429                    || (*p == '-')))
   1430         {
 ► 1431           name[p - b] = *p;
   1432           p++;
   1433         }
   1434       name[p - b] = '\0';
   1435       
   1436       /* Check for the name in the enum types.  */
```

## asan report

```txt
=================================================================
==30740==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fffe1708284 at pc 0x7fad107697b4 bp 0x7fffe17081d0 sp 0x7fffe17081c8
WRITE of size 1 at 0x7fffe1708284 thread T0
    #0 0x7fad107697b3 in rec_type_check_enum /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-types.c:1431:23
    #1 0x7fad107697b3 in rec_type_check /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-types.c:640
    #2 0x7fad107400c5 in rec_int_check_field_type /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:307:16
    #3 0x7fad1073e100 in rec_int_check_record_types /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:383:12
    #4 0x7fad1073e100 in rec_int_check_record /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:230
    #5 0x7fad1073ce40 in rec_int_check_rset /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:202:14
    #6 0x7fad1073930b in rec_int_check_db /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-int.c:112:19
    #7 0x5181bf in recfix_check_database /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:344:10
    #8 0x5181bf in recfix_do_auto /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:521
    #9 0x5181bf in main /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/utils/recfix.c:558
    #10 0x7fad0f59eb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #11 0x41c3e9 in _start (/home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/installed-asan/bin/recfix+0x41c3e9)

Address 0x7fffe1708284 is located in stack of thread T0 at offset 164 in frame
    #0 0x7fad1076823f in rec_type_check /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-types.c:577

  This frame has 9 object(s):
    [32, 48) 'uu.i' (line 1222)
    [64, 164) 'name.i' (line 1412) <== Memory access at offset 164 overflows this variable
    [208, 224) 'tm.i' (line 1372)
    [240, 248) 'tmp.i80' (line 1314)
    [272, 280) 'p.i' (line 1261)
    [304, 308) 'num.i' (line 1262)
    [320, 328) 'tmp.i' (line 1263)
    [352, 360) 'err_str' (line 580)
    [384, 392) 'errors_size' (line 581)
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/pwd/gnu-fuzz/recutils/recutils-1.8.patch/src/rec-types.c:1431:23 in rec_type_check_enum
Shadow bytes around the buggy address:
  0x10007c2d9000: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007c2d9010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007c2d9020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007c2d9030: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x10007c2d9040: f8 f8 f2 f2 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10007c2d9050:[04]f2 f2 f2 f2 f2 f8 f8 f2 f2 f8 f2 f2 f2 f8 f2
  0x10007c2d9060: f2 f2 f8 f2 f8 f2 f2 f2 00 f2 f2 f2 00 f3 f3 f3
  0x10007c2d9070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007c2d9080: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 00 f2 f2 f2
  0x10007c2d9090: f8 f2 f2 f2 f8 f3 f3 f3 00 00 00 00 00 00 00 00
  0x10007c2d90a0: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
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
==30740==ABORTING

```

