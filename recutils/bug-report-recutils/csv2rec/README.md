
# Description
None
# version
None

# others
## @_@
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamseri0us360@gmail.com if you have some question.

# Detial

# [vuln/field_cb@csv2rec.c:264-34___heap-buffer-overflow](#description)
## target
```
csv2rec @@
```
## gdb info
```c
In file: /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c
   259                        _("%s: %lu: this line contains %lu fields, but %lu header fields were read\n"),
   260                        source,
   261                        ctx->lineno, ctx->num_field_names, ctx->num_fields);
   262               exit (EXIT_FAILURE);
   263             }
 ► 264           field = rec_field_new (ctx->field_names[ctx->num_fields], str);
   265           rec_mset_append (rec_record_mset (ctx->record), MSET_FIELD, (void *) field, MSET_ANY);
   266         }
   267 
   268       ctx->num_fields++;
   269     }

```
## asan report
```txt
=================================================================
==6141==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6280026bb900 at pc 0x000000518153 bp 0x7ffe8a42ca10 sp 0x7ffe8a42ca08
READ of size 8 at 0x6280026bb900 thread T0
    #0 0x518152 in field_cb /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c:264:34
    #1 0x58d2f3 in csv_parse /home/pwd/gnu-fuzz/recutils/recutils-1.8/libcsv/libcsv.c
    #2 0x517729 in process_csv /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c:374:11
    #3 0x517729 in main /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c:395
    #4 0x7f3a03064b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41c469 in _start (/home/pwd/gnu-fuzz/recutils/recutils-1.8/installed-asan/bin/csv2rec+0x41c469)

0x6280026bb900 is located 0 bytes to the right of 14336-byte region [0x6280026b8100,0x6280026bb900)
allocated by thread T0 here:
    #0 0x4dc7a0 in realloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:107
    #1 0x517bc8 in field_cb /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c:214:11

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/gnu-fuzz/recutils/recutils-1.8/utils/csv2rec.c:264:34 in field_cb
Shadow bytes around the buggy address:
  0x0c50804cf6d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c50804cf6e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c50804cf6f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c50804cf700: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c50804cf710: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c50804cf720:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c50804cf730: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c50804cf740: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c50804cf750: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c50804cf760: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c50804cf770: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==6141==ABORTING


```


