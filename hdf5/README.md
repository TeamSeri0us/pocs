## Description
HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data. HDF5 is portable and is extensible, allowing applications to evolve in their use of HDF5. The HDF5 Technology suite includes tools and applications for managing, manipulating, viewing, and analyzing data in the HDF5 format.
link: https://portal.hdfgroup.org/display/HDF5/HDF5
## version
h5dump: Version 1.8.20

## others
this bug is reported by pwd@360TeamSeri0us, 
please send email to   teamSeri0us360@gmail.com if you have some quetion.

## Test Target
./h5dump-shared $file

## vuln/H5O_link_decode-memcpy-param-overlap
```
=================================================================
==5985==ERROR: AddressSanitizer: memcpy-param-overlap: memory ranges [0x60b000000e00,0x60b000000e6b) and [0x60b000000d9c, 0x60b000000e07) overlap
    #0 0x4dc94c in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7fc649c1466d in H5O_link_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Olink.c:203:5
    #2 0x7fc649c20f39 in H5O_msg_iterate_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1304:13
    #3 0x7fc649c2209d in H5O_msg_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1233:21
    #4 0x7fc649a517c5 in H5G_compact_build_table /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:156:12
    #5 0x7fc649a52c5a in H5G__compact_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:422:8
    #6 0x7fc649a9b47d in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:695:29
    #7 0x7fc649a7ad32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #8 0x7fc64a20390c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #9 0x7fc64a726e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #10 0x7fc64a72aba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #11 0x7fc64a7231c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #12 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #13 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #14 0x7fc6486c7b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #15 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x60b000000e00 is located 0 bytes inside of 108-byte region [0x60b000000e00,0x60b000000e6c)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fc64a213758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21
    #2 0x7fc649c20f39 in H5O_msg_iterate_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1304:13
    #3 0x7fc649c2209d in H5O_msg_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1233:21

0x60b000000db8 is located 0 bytes to the right of 104-byte region [0x60b000000d50,0x60b000000db8)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fc64a213758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: memcpy-param-overlap /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
==5985==ABORTING
```


## vuln/H5O_link_decode-heap-buffer-overflow

```
=================================================================
==36563==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60b000000db8 at pc 0x0000004dcd22 bp 0x7ffd68475dd0 sp 0x7ffd68475580
READ of size 1954047240 at 0x60b000000db8 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7fdeb47b566d in H5O_link_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Olink.c:203:5
    #2 0x7fdeb47c1f39 in H5O_msg_iterate_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1304:13
    #3 0x7fdeb47c309d in H5O_msg_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:1233:21
    #4 0x7fdeb45f27c5 in H5G_compact_build_table /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:156:12
    #5 0x7fdeb45f3c5a in H5G__compact_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:422:8
    #6 0x7fdeb463c47d in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:695:29
    #7 0x7fdeb461bd32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #8 0x7fdeb4da490c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #9 0x7fdeb52c7e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #10 0x7fdeb52cbba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #11 0x7fdeb52c41c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #12 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #13 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #14 0x7fdeb3268b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #15 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x60b000000db8 is located 0 bytes to the right of 104-byte region [0x60b000000d50,0x60b000000db8)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fdeb4db4758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c167fff8160: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c167fff8170: 00 00 00 00 00 00 fa fa fa fa fa fa fa fa 00 00
  0x0c167fff8180: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
  0x0c167fff8190: fa fa fa fa 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c167fff81a0: 06 fa fa fa fa fa fa fa fa fa 00 00 00 00 00 00
=>0x0c167fff81b0: 00 00 00 00 00 00 00[fa]fa fa fa fa fa fa fa fa
  0x0c167fff81c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff81d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff81e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff81f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff8200: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==36563==ABORTING

```

## vuln/H5O_chunk_deserialize-global-buffer-overflow

```
=================================================================
==62773==ERROR: AddressSanitizer: global-buffer-overflow on address 0x7f38844a1068 at pc 0x7f3883aa1c92 bp 0x7fffe30274f0 sp 0x7fffe30274e8
READ of size 8 at 0x7f38844a1068 thread T0
    #0 0x7f3883aa1c91 in H5O_chunk_deserialize /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Ocache.c:1132:20
    #1 0x7f3883a9c1c9 in H5O_cache_chk_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Ocache.c:721:12
    #2 0x7f388408e728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #3 0x7f388408e728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #4 0x7f38837268ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #5 0x7f3883a5bc03 in H5O_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:1724:58
    #6 0x7f3883a4eae8 in H5O_get_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:2803:22
    #7 0x7f3883956c1c in H5G_loc_info_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:699:8
    #8 0x7f388398f068 in H5G_traverse_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:777:8
    #9 0x7f388398c24a in H5G_traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:858:8
    #10 0x7f3883956951 in H5G_loc_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:744:8
    #11 0x7f3883a4d37a in H5Oget_info_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:659:8
    #12 0x51994f in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1468:12
    #13 0x7f388259ab96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #14 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

Address 0x7f38844a1068 is a wild pointer.
SUMMARY: AddressSanitizer: global-buffer-overflow /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Ocache.c:1132:20 in H5O_chunk_deserialize
Shadow bytes around the buggy address:
  0x0fe79088c1b0: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c1c0: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c1d0: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c1e0: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c1f0: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
=>0x0fe79088c200: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9[f9]f9 f9
  0x0fe79088c210: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c220: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c230: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c240: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
  0x0fe79088c250: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
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
==62773==ABORTING

```

## vuln/H5FD_sec2_read-stack-buffer-overflow

```
708:        if(0 == bytes_read) {
709:            /* end of file but not end of format address space */
710:            HDmemset(buf, 0, size);
711:            break;
712:        } /* end if */



=================================================================
==100641==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe0b90dc50 at pc 0x0000004dd0ac bp 0x7ffe0b90d510 sp 0x7ffe0b90ccc0
WRITE of size 4197 at 0x7ffe0b90dc50 thread T0
    #0 0x4dd0ab in __asan_memset /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:27
    #1 0x7f7e12da9e97 in H5FD_sec2_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FDsec2.c:710:13
    #2 0x7f7e12d82a8c in H5FD_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FDint.c:208:8
    #3 0x7f7e12d58484 in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:376:16
    #4 0x7f7e1354c728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #5 0x7f7e1354c728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #6 0x7f7e12be48ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #7 0x7f7e12d4ce56 in H5F_super_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper.c:291:41
    #8 0x7f7e12d2a466 in H5F_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fint.c:1084:12
    #9 0x7f7e12d14b74 in H5Fopen /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5F.c:601:28
    #10 0x7f7e13a77f79 in h5tools_fopen /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools.c:567:23
    #11 0x5196c8 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1429:15
    #12 0x7f7e11a58b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #13 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

Address 0x7ffe0b90dc50 is located in stack of thread T0 at offset 1424 in frame
    #0 0x7f7e12d52e4f in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:112

  This frame has 13 object(s):
    [32, 166) 'sbuf' (line 115)
    [240, 248) 'stored_eoa' (line 120)
    [272, 273) 'sizeof_addr' (line 122)
    [288, 289) 'sizeof_size' (line 123)
    [304, 312) 'p' (line 126)
    [336, 340) 'super_vers' (line 127)
    [352, 360) 'btree_k' (line 196)
    [384, 388) 'sym_leaf_k' (line 197)
    [400, 1424) 'dbuf' (line 335)
    [1552, 1561) 'drv_name' (line 336) <== Memory access at offset 1424 partially underflows this variable
    [1584, 1608) 'ext_loc' (line 486) <== Memory access at offset 1424 partially underflows this variable
    [1648, 1660) 'btreek' (line 487) <== Memory access at offset 1424 partially underflows this variable
    [1680, 1712) 'drvinfo' (line 488) <== Memory access at offset 1424 partially underflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:27 in __asan_memset
Shadow bytes around the buggy address:
  0x100041719b30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719b40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719b50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719b60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719b70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x100041719b80: 00 00 00 00 00 00 00 00 00 00[f2]f2 f2 f2 f2 f2
  0x100041719b90: f2 f2 f2 f2 f2 f2 f2 f2 f2 f2 00 01 f2 f2 f8 f8
  0x100041719ba0: f8 f2 f2 f2 f2 f2 f8 f8 f2 f2 f8 f8 f8 f8 f3 f3
  0x100041719bb0: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719bc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100041719bd0: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 04 f2 04 f3
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
==100641==ABORTING

```

## vuln/H5G_ent_decode-heap-buffer-overflow

```
=================================================================
==129741==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6130000001a0 at pc 0x7feb13c16b52 bp 0x7ffcdd72ebf0 sp 0x7ffcdd72ebe8
WRITE of size 8 at 0x6130000001a0 thread T0
    #0 0x7feb13c16b51 in H5G_ent_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gent.c:147:5
    #1 0x7feb13c15e75 in H5G__ent_decode_vec /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gent.c:108:12
    #2 0x7feb13bf3f68 in H5G_node_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcache.c:181:8
    #3 0x7feb14360728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #4 0x7feb14360728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #5 0x7feb139f88ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #6 0x7feb13c360e9 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:982:36
    #7 0x7feb13a07bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #8 0x7feb13a07602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #9 0x7feb13c4f785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #10 0x7feb13c4037a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #11 0x7feb13c1fd32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #12 0x7feb143a890c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #13 0x7feb148cbe44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #14 0x7feb148cfba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #15 0x7feb148c81c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #16 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #17 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #18 0x7feb1286cb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #19 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x6130000001a0 is located 24 bytes to the right of 328-byte region [0x613000000040,0x613000000188)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7feb143b8758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gent.c:147:5 in H5G_ent_decode
Shadow bytes around the buggy address:
  0x0c267fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff8000: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c267fff8010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c267fff8020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c267fff8030: 00 fa fa fa[fa]fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c267fff8080: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==129741==ABORTING

```

## vuln/H5O_fill_old_decode-heap-buffer-overflow

```
=================================================================
==14782==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x612000026558 at pc 0x0000004dcd22 bp 0x7ffeb8aaf230 sp 0x7ffeb8aae9e0
READ of size 8388612 at 0x612000026558 thread T0
    #0 0x4dcd21 in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x7fa7935879a0 in H5O_fill_old_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Ofill.c:325:9
    #2 0x7fa7935879a0 in H5O_fill_shared_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Oshared.h:82
    #3 0x7fa7935a30ba in H5O_msg_read_oh /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:543:5
    #4 0x7fa7935a27d0 in H5O_msg_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Omessage.c:481:29
    #5 0x7fa7932aa283 in H5D__open_oid /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1403:24
    #6 0x7fa7932aa283 in H5D_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dint.c:1256
    #7 0x7fa79323ad7e in H5Dopen2 /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5D.c:366:24
    #8 0x7fa7940a99b0 in find_objs_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:505:28
    #9 0x7fa7940b2289 in traverse_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:219:16
    #10 0x7fa793401cf7 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:937:17
    #11 0x7fa7934173f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #12 0x7fa7931e8bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #13 0x7fa7931e8602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #14 0x7fa793430785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #15 0x7fa79342137a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #16 0x7fa793400d32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #17 0x7fa793b8990c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #18 0x7fa7940ace44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #19 0x7fa7940b0ba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #20 0x7fa7940a91c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #21 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #22 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #23 0x7fa79204db96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #24 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x612000026558 is located 0 bytes to the right of 280-byte region [0x612000026440,0x612000026558)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fa793b99758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c247fffcc50: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fffcc70: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
  0x0c247fffcc80: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fffcc90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c247fffcca0: 00 00 00 00 00 00 00 00 00 00 00[fa]fa fa fa fa
  0x0c247fffccb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffccc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffccd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffcce0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fffccf0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==14782==ABORTING
```
## vuln/H5VM_memcpyvv-OUT_OF_BOUND_READ

```
#equal:
#        acc_len = 0;
#        do {
#            /* Copy data */
#           HDmemcpy(dst, src, tmp_dst_len);  /*Line 1667*/

AddressSanitizer:DEADLYSIGNAL
=================================================================
==74563==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f0eda3846c4 bp 0x7ffc5fa97a10 sp 0x7ffc5fa97198 T0)
==74563==The signal is caused by a READ memory access.
==74563==Hint: address points to the zero page.
    #0 0x7f0eda3846c3  (/lib/x86_64-linux-gnu/libc.so.6+0xbb6c3)
    #1 0x4dc8cd in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #2 0x7f0edbe9cde4 in H5VM_memcpyvv /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5VM.c:1667:13
    #3 0x7f0edb4e10e0 in H5D__compact_readvv /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dcompact.c:298:21
    #4 0x7f0edb567d20 in H5D__gather_file /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dscatgath.c:249:12
    #5 0x7f0edb56579b in H5D__scatgath_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dscatgath.c:512:13
    #6 0x7f0edb523268 in H5D__contig_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dcontig.c:540:8
    #7 0x7f0edb5571a3 in H5D__read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dio.c:604:8
    #8 0x7f0edb554f72 in H5Dread /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Dio.c:222:10
    #9 0x7f0edc327191 in h5tools_dump_simple_dset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:1611:13
    #10 0x7f0edc327191 in h5tools_dump_dset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:1786
    #11 0x7f0edc335040 in h5tools_dump_data /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_dump.c:3757:18
    #12 0x528ce2 in dump_dataset /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:1064:21
    #13 0x52436c in dump_all_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c:356:17
    #14 0x7f0edb69cb55 in H5G_iterate_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:780:29
    #15 0x7f0edb6b43f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #16 0x7f0edb485bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #17 0x7f0edb485602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #18 0x7f0edb6cd785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #19 0x7f0edb6be37a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #20 0x7f0edb69beaa in H5G_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:841:21
    #21 0x7f0edbe23f7d in H5Literate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1180:21
    #22 0x5276e5 in dump_group /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump_ddl.c
    #23 0x51a276 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1547:17
    #24 0x7f0eda2eab96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #25 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0xbb6c3) 
==74563==ABORTING

```


## vuln/H5F_addr_decode_len-stack-buffer-overflow

```
==80179==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==80179==Installed the sigaction for signal 11
==80179==Installed the sigaction for signal 7
==80179==Installed the sigaction for signal 8
==80179==T0: stack [0x7ffeda666000,0x7ffedae66000) size 0x800000; local=0x7ffedae62fe8
==80179==AddressSanitizer Init done
=================================================================
==80179==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffedae60c86 at pc 0x7fe3e6f4653d bp 0x7ffedae60b30 sp 0x7ffedae60b28
READ of size 1 at 0x7ffedae60c86 thread T0
    #0 0x7fe3e6f4653c in H5F_addr_decode_len /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fint.c:1752:6
    #1 0x7fe3e6f4653c in H5F_addr_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fint.c:1807
    #2 0x7fe3e7018671 in H5G_ent_decode /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gent.c:161:13
    #3 0x7fe3e6f6c885 in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:291:12
    #4 0x7fe3e7762728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #5 0x7fe3e7762728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #6 0x7fe3e6dfa8ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #7 0x7fe3e6f62e56 in H5F_super_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper.c:291:41
    #8 0x7fe3e6f40466 in H5F_open /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fint.c:1084:12
    #9 0x7fe3e6f2ab74 in H5Fopen /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5F.c:601:28
    #10 0x7fe3e7c8df79 in h5tools_fopen /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools.c:567:23
    #11 0x5196c8 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1429:15
    #12 0x7fe3e5c6eb96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #13 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

Address 0x7ffedae60c86 is located in stack of thread T0 at offset 166 in frame
    #0 0x7fe3e6f68e4f in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:112

  This frame has 13 object(s):
    [32, 166) 'sbuf' (line 115) <== Memory access at offset 166 overflows this variable
    [240, 248) 'stored_eoa' (line 120)
    [272, 273) 'sizeof_addr' (line 122)
    [288, 289) 'sizeof_size' (line 123)
    [304, 312) 'p' (line 126)
    [336, 340) 'super_vers' (line 127)
    [352, 360) 'btree_k' (line 196)
    [384, 388) 'sym_leaf_k' (line 197)
    [400, 1424) 'dbuf' (line 335)
    [1552, 1561) 'drv_name' (line 336)
    [1584, 1608) 'ext_loc' (line 486)
    [1648, 1660) 'btreek' (line 487)
    [1680, 1712) 'drvinfo' (line 488)
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fint.c:1752:6 in H5F_addr_decode_len
Shadow bytes around the buggy address:
  0x10005b5c4140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10005b5c4150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10005b5c4160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10005b5c4170: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x10005b5c4180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10005b5c4190:[06]f2 f2 f2 f2 f2 f2 f2 f2 f2 00 f2 f2 f2 01 f2
  0x10005b5c41a0: 01 f2 00 f2 f2 f2 04 f2 00 f2 f2 f2 04 f2 f8 f8
  0x10005b5c41b0: f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8
  0x10005b5c41c0: f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8
  0x10005b5c41d0: f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8
  0x10005b5c41e0: f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8 f8
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
==80179==ABORTING

```

## vuln/H5F__accum_read-Out_Of_Bound_Read

```
==129075==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==129075==Installed the sigaction for signal 11
==129075==Installed the sigaction for signal 7
==129075==Installed the sigaction for signal 8
==129075==T0: stack [0x7ffeee8d4000,0x7ffeef0d4000) size 0x800000; local=0x7ffeef0d1548
==129075==AddressSanitizer Init done
AddressSanitizer:DEADLYSIGNAL
=================================================================
==129075==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fbc8870b6c4 bp 0x7ffeef0d0340 sp 0x7ffeef0cfac8 T0)
==129075==The signal is caused by a READ memory access.
==129075==Hint: address points to the zero page.
    #0 0x7fbc8870b6c3  (/lib/x86_64-linux-gnu/libc.so.6+0xbb6c3)
    #1 0x4dc8cd in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #2 0x7fbc8994b819 in H5F__accum_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Faccum.c:202:17
    #3 0x7fbc8995bfa3 in H5F_block_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fio.c:117:8
    #4 0x7fbc89b028fc in H5HL_datablock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HLcache.c:652:12
    #5 0x7fbc8a165728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #6 0x7fbc8a165728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #7 0x7fbc897fd8ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #8 0x7fbc89af699a in H5HL_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HL.c:487:47
    #9 0x7fbc89a541f0 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:547:24
    #10 0x7fbc89a4537a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #11 0x7fbc89a24d32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #12 0x7fbc8a1ad90c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #13 0x7fbc8a6d0e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #14 0x7fbc8a6d4ba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #15 0x7fbc8a6cd1c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #16 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #17 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #18 0x7fbc88671b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #19 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/lib/x86_64-linux-gnu/libc.so.6+0xbb6c3) 
==129075==ABORTING

```

## vuln/H5FL_blk_malloc-heap-buffer-overflow

```
==22434==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==22434==Installed the sigaction for signal 11
==22434==Installed the sigaction for signal 7
==22434==Installed the sigaction for signal 8
==22434==T0: stack [0x7ffe4b043000,0x7ffe4b843000) size 0x800000; local=0x7ffe4b841b78
==22434==AddressSanitizer Init done
=================================================================
==22434==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000004c50 at pc 0x7fbfd8cf2986 bp 0x7ffe4b83eff0 sp 0x7ffe4b83efe8
WRITE of size 8 at 0x602000004c50 thread T0
    #0 0x7fbfd8cf2985 in H5FL_blk_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FL.c:891:15
    #1 0x7fbfd86782d7 in H5HL_prefix_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HLcache.c:328:44
    #2 0x7fbfd8cde728 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #3 0x7fbfd8cde728 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #4 0x7fbfd83768ad in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #5 0x7fbfd86769cd in H5HL_heapsize /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HL.c:1207:39
    #6 0x7fbfd85ce924 in H5G__stab_bh_size /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:685:8
    #7 0x7fbfd85c5179 in H5O_group_bh_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Goh.c:400:12
    #8 0x7fbfd869ee48 in H5O_get_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:2879:16
    #9 0x7fbfd85a6c1c in H5G_loc_info_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:699:8
    #10 0x7fbfd85df514 in H5G_traverse_real /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:638:16
    #11 0x7fbfd85dc24a in H5G_traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gtraverse.c:858:8
    #12 0x7fbfd85a6951 in H5G_loc_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gloc.c:744:8
    #13 0x7fbfd869d37a in H5Oget_info_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5O.c:659:8
    #14 0x7fbfd924ecfb in traverse_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:204:12
    #15 0x7fbfd859ecf7 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:937:17
    #16 0x7fbfd85b43f2 in H5G__node_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gnode.c:1004:25
    #17 0x7fbfd8385bc4 in H5B_iterate_helper /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1173:25
    #18 0x7fbfd8385602 in H5B_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5B.c:1218:21
    #19 0x7fbfd85cd785 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:563:25
    #20 0x7fbfd85be37a in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #21 0x7fbfd859dd32 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #22 0x7fbfd8d2690c in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #23 0x7fbfd9249e44 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #24 0x7fbfd924dba2 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #25 0x7fbfd92461c3 in init_objs /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5tools_utils.c:577:12
    #26 0x5165a5 in table_list_add /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:404:8
    #27 0x519992 in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5dump/h5dump.c:1475:12
    #28 0x7fbfd71eab96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #29 0x41dfa9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-build/installed/bin/h5dump-shared+0x41dfa9)

0x602000004c57 is located 0 bytes to the right of 7-byte region [0x602000004c50,0x602000004c57)
allocated by thread T0 here:
    #0 0x4dde60 in malloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:88
    #1 0x7fbfd8d36758 in H5MM_malloc /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5MM.c:64:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FL.c:891:15 in H5FL_blk_malloc
Shadow bytes around the buggy address:
  0x0c047fff8930: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
  0x0c047fff8940: fa fa 00 00 fa fa 02 fa fa fa 00 fa fa fa 00 00
  0x0c047fff8950: fa fa 00 00 fa fa 00 00 fa fa fd fa fa fa 00 00
  0x0c047fff8960: fa fa 00 00 fa fa 04 fa fa fa 05 fa fa fa 05 fa
  0x0c047fff8970: fa fa 04 fa fa fa 00 05 fa fa 00 00 fa fa 00 05
=>0x0c047fff8980: fa fa 00 00 fa fa 00 00 fa fa[07]fa fa fa fa fa
  0x0c047fff8990: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff89a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff89b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff89c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff89d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==22434==ABORTING

```

## vuln/H5FD_sec2_read-2-stack-buffer-overflow


```
660:        H5FD_sec2_t     *file       = (H5FD_sec2_t *)_file;
...
696:        do {
697:            bytes_read = HDread(file->fd, buf, bytes_in);
698:        } while(-1 == bytes_read && EINTR == errno);


==38816==AddressSanitizer: libc interceptors initialized
|| `[0x10007fff8000, 0x7fffffffffff]` || HighMem    ||
|| `[0x02008fff7000, 0x10007fff7fff]` || HighShadow ||
|| `[0x00008fff7000, 0x02008fff6fff]` || ShadowGap  ||
|| `[0x00007fff8000, 0x00008fff6fff]` || LowShadow  ||
|| `[0x000000000000, 0x00007fff7fff]` || LowMem     ||
MemToShadow(shadow): 0x00008fff7000 0x000091ff6dff 0x004091ff6e00 0x02008fff6fff
redzone=16
max_redzone=2048
quarantine_size_mb=256M
thread_local_quarantine_size_kb=1024K
malloc_context_size=30
SHADOW_SCALE: 3
SHADOW_GRANULARITY: 8
SHADOW_OFFSET: 0x7fff8000
==38816==Installed the sigaction for signal 11
==38816==Installed the sigaction for signal 7
==38816==Installed the sigaction for signal 8
==38816==T0: stack [0x7fff51477000,0x7fff51c77000) size 0x800000; local=0x7fff51c754d8
==38816==AddressSanitizer Init done
=================================================================
==38816==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff51c73650 at pc 0x00000048c205 bp 0x7fff51c72f10 sp 0x7fff51c726c0
WRITE of size 1908 at 0x7fff51c73650 thread T0
    #0 0x48c204 in __interceptor_read.part.46 /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/../sanitizer_common/sanitizer_common_interceptors.inc:960
    #1 0x7f394b9b68ae in H5FD_sec2_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FDsec2.c:697:26
    #2 0x7f394b98fa8c in H5FD_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5FDint.c:208:8
    #3 0x7f394b965484 in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:376:16

Address 0x7fff51c73650 is located in stack of thread T0 at offset 1424 in frame
    #0 0x7f394b95fe4f in H5F_sblock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fsuper_cache.c:112

  This frame has 13 object(s):
    [32, 166) 'sbuf' (line 115)
    [240, 248) 'stored_eoa' (line 120)
    [272, 273) 'sizeof_addr' (line 122)
    [288, 289) 'sizeof_size' (line 123)
    [304, 312) 'p' (line 126)
    [336, 340) 'super_vers' (line 127)
    [352, 360) 'btree_k' (line 196)
    [384, 388) 'sym_leaf_k' (line 197)
    [400, 1424) 'dbuf' (line 335)
    [1552, 1561) 'drv_name' (line 336) <== Memory access at offset 1424 partially underflows this variable
    [1584, 1608) 'ext_loc' (line 486) <== Memory access at offset 1424 partially underflows this variable
    [1648, 1660) 'btreek' (line 487) <== Memory access at offset 1424 partially underflows this variable
    [1680, 1712) 'drvinfo' (line 488) <== Memory access at offset 1424 partially underflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/../sanitizer_common/sanitizer_common_interceptors.inc:960 in __interceptor_read.part.46
Shadow bytes around the buggy address:
  0x10006a386670: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a386680: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a386690: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a3866a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a3866b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10006a3866c0: 00 00 00 00 00 00 00 00 00 00[f2]f2 f2 f2 f2 f2
  0x10006a3866d0: f2 f2 f2 f2 f2 f2 f2 f2 f2 f2 00 01 f2 f2 f8 f8
  0x10006a3866e0: f8 f2 f2 f2 f2 f2 f8 f8 f2 f2 f8 f8 f8 f8 f3 f3
  0x10006a3866f0: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a386700: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10006a386710: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 04 f2 04 f3
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
==38816==ABORTING

```
