## Description
HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data. HDF5 is portable and is extensible, allowing applications to evolve in their use of HDF5. The HDF5 Technology suite includes tools and applications for managing, manipulating, viewing, and analyzing data in the HDF5 format.
link: https://portal.hdfgroup.org/display/HDF5/HDF5
## version
h5dump: Version 1.8.20

## others
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.i
And thanks for reminding of Josh

## Test Target
./h5dump-shared $file

## vuln2/H5O_sdspace_decode-heap-buffer-overflow 
### src
```
for(i = 0; i < sdim->rank; i++)
    H5F_DECODE_LENGTH (f, p, sdim->max[i]);
```
### asan report
```
=================================================================
==7201==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61200002625f at pc 0x7f7cd6d3f2c6 bp 0x7ffeaae03800 sp 0x7ffeaae037f8
READ of size 1 at 0x61200002625f thread T0
    #0 0x7f7cd6d3f2c5 in H5O_sdspace_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Osdspace.c:175:17
    #1 0x7f7cd6d3f2c5 in H5O_sdspace_shared_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Oshared.h:82
    #2 0x7f7cd6d290ea in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #3 0x7f7cd6d287fd in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29
    #4 0x7f7cd6df402e in H5S_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5S.c:1085:8
    #5 0x7f7cd6a2eed9 in H5D__open_oid /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1370:42
    #6 0x7f7cd6a2eed9 in H5D_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1256
    #7 0x7f7cd69c0d5e in H5Dopen2 /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5D.c:366:24
    #8 0x7f7cd782f9c0 in find_objs_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:505:28
    #9 0x7f7cd7838299 in traverse_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:219:16
    #10 0x7f7cd6b87cf7 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:937:17
    #11 0x7f7cd6b9d3f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #12 0x7f7cd696ebb4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #13 0x7f7cd696e5f2 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #14 0x7f7cd6bb6785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #15 0x7f7cd6ba737a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #16 0x7f7cd6b86d32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #17 0x7f7cd730f91c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #18 0x7f7cd7832e54 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #19 0x7f7cd7836bb2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #20 0x7f7cd782f1d3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #21 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #22 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #23 0x7f7cd57d3b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #24 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-asan/installed/bin/h5dump-shared+0x41dfa9)

0x61200002625f is located 7 bytes to the right of 280-byte region [0x612000026140,0x612000026258)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7f7cd731f768 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Osdspace.c:175:17 in H5O_sdspace_decode
Shadow bytes around the buggy address:
  0x0c247fffcbf0: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fffcc10: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
  0x0c247fffcc20: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c247fffcc40: 00 00 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa
  0x0c247fffcc50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc80: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcc90: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==7201==ABORTING

```
