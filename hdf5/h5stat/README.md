# Description
HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data. HDF5 is portable and is extensible, allowing applications to evolve in their use of HDF5. The HDF5 Technology suite includes tools and applications for managing, manipulating, viewing, and analyzing data in the HDF5 format.
link: https://portal.hdfgroup.org/display/HDF5/HDF5
# version
h5dump: Version 1.8.20

# others
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have some quetion.


# [vuln/H5F__accum_read@H5Faccum.c:202-17___out-of-bounds-read](#description)
## target
```
h5stat @@
```
## gdb info
```

backtrace:
#0  __memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:332
#1  0x000055555560f28d in H5F__accum_read (fio_info=0x7fffffffcd60, type=H5FD_MEM_LHEAP, addr=18446744073709551615, size=256, buf=0x555555b5d778) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Faccum.c:202
#2  0x0000555555613219 in H5F_block_read (f=0x555555b5ab30, type=H5FD_MEM_LHEAP, addr=18446744073709551615, size=256, dxpl_id=167772168, buf=0x555555b5d778) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fio.c:117
#3  0x000055555567d0e2 in H5HL_datablock_load (f=0x555555b5ab30, dxpl_id=167772168, addr=18446744073709551615, _udata=0x7fffffffcfb0) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HLcache.c:652
#4  0x000055555582f45e in H5C_load_entry (f=0x555555b5ab30, dxpl_id=167772168, type=0x555555b145a0 <H5AC_LHEAP_DBLK>, addr=18446744073709551615, udata=0x7fffffffcfb0) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950
#5  0x0000555555827af7 in H5C_protect (f=0x555555b5ab30, primary_dxpl_id=167772168, secondary_dxpl_id=167772168, type=0x555555b145a0 <H5AC_LHEAP_DBLK>, addr=18446744073709551615, udata=0x7fffffffcfb0, flags=512) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
#6  0x00005555555ae407 in H5AC_protect (f=0x555555b5ab30, dxpl_id=167772168, type=0x555555b145a0 <H5AC_LHEAP_DBLK>, addr=18446744073709551615, udata=0x7fffffffcfb0, rw=H5AC_READ) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250
#7  0x000055555567911c in H5HL_protect (f=0x555555b5ab30, dxpl_id=167772168, addr=96, rw=H5AC_READ) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HL.c:487
#8  0x000055555564d907 in H5G__stab_iterate (oloc=0x555555b5d2d8, dxpl_id=167772168, order=H5_ITER_INC, skip=0, last_lnk=0x0, op=0x55555563e2b5 <H5G_visit_cb>, op_data=0x7fffffffd210) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:547
#9  0x0000555555649e4e in H5G__obj_iterate (grp_oloc=0x555555b5d2d8, idx_type=H5_INDEX_NAME, order=H5_ITER_INC, skip=0, last_lnk=0x0, op=0x55555563e2b5 <H5G_visit_cb>, op_data=0x7fffffffd210, dxpl_id=167772168) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705
#10 0x000055555563f244 in H5G_visit (loc_id=16777216, group_name=0x5555558a85a0 "/", idx_type=H5_INDEX_NAME, order=H5_ITER_INC, op=0x5555555983d5 <traverse_cb>, op_data=0x7fffffffd340, lapl_id=167772160, dxpl_id=167772168) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172
#11 0x000055555583dc41 in H5Lvisit_by_name (loc_id=16777216, group_name=0x5555558a85a0 "/", idx_type=H5_INDEX_NAME, order=H5_ITER_INC, op=0x5555555983d5 <traverse_cb>, op_data=0x7fffffffd340, lapl_id=167772160) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376
#12 0x000055555559895e in traverse (file_id=16777216, grp_name=0x5555558a85a0 "/", visit_start=1, recurse=1, visitor=0x7fffffffd460) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289
#13 0x000055555559a0af in h5trav_visit (fid=16777216, grp_name=0x5555558a85a0 "/", visit_start=1, recurse=1, visit_obj=0x55555557eca1 <obj_stats>, visit_lnk=0x55555557ed6d <lnk_stats>, udata=0x7fffffffd4f0) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061
#14 0x0000555555580b50 in main (argc=2, argv=0x7fffffffd898) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5stat/h5stat.c:1618
#15 0x00007ffff7463b97 in __libc_start_main (main=0x555555580742 <main>, argc=2, argv=0x7fffffffd898, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffd888) at ../csu/libc-start.c:310
#16 0x000055555557dc4a in _start ()

src info:
327	in ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S

register info:
rax            0x555555b5d778	93824998561656
rbx            0x555555b5d120	93824998560032
rcx            0x0	0
rdx            0x100	256
rsi            0x0	0
rdi            0x555555b5d778	93824998561656
rbp            0x7fffffffcd10	0x7fffffffcd10
rsp            0x7fffffffcc78	0x7fffffffcc78
r8             0x555555b5d778	93824998561656
r9             0x555555b5d778	93824998561656
r10            0x555555b1e010	93824998301712
r11            0x0	0
r12            0x55555557dc20	93824992402464
r13            0x7fffffffd890	140737488345232
r14            0x0	0
r15            0x0	0
rip            0x7ffff75d0ba5	0x7ffff75d0ba5 <__memmove_avx_unaligned_erms+213>
eflags         0x10202	[ IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0

```
## asan report
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==21308==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fc4436626c4 bp 0x7ffde0b1b200 sp 0x7ffde0b1a988 T0)
==21308==The signal is caused by a READ memory access.
==21308==Hint: address points to the zero page.
    #0 0x7fc4436626c3  /build/glibc-OTsEL5/glibc-2.27/string/../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:418
    #1 0x4fa7fd in __asan_memcpy /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #2 0x6e0709 in H5F__accum_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Faccum.c:202:17
    #3 0x6ed123 in H5F_block_read /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Fio.c:117:8
    #4 0x83db1c in H5HL_datablock_load /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HLcache.c:652:12
    #5 0xe69f38 in H5C_load_entry /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:7950:25
    #6 0xe69f38 in H5C_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5C.c:3568
    #7 0x5c351d in H5AC_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5AC.c:1250:13
    #8 0x831bba in H5HL_protect /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5HL.c:487:47
    #9 0x7a9e50 in H5G__stab_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gstab.c:547:24
    #10 0x79d7ba in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:705:25
    #11 0x77d172 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #12 0xeae3ac in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #13 0x57dba4 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #14 0x581902 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #15 0x53595a in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5stat/h5stat.c:1618:16
    #16 0x7fc4435c8b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #17 0x43bed9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-asan/installed/bin/h5stat+0x43bed9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /build/glibc-OTsEL5/glibc-2.27/string/../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:418 
==21308==ABORTING

```




# [vuln/H5L_extern_query@H5Lexternal.c:498-10___out-of-bounds-read](#description)
## target
```
h5stat @@
```
## gdb info
```

backtrace:
#0  0x0000555555843d29 in H5L_extern_query (link_name=0x555555b5d3d0 "ext_l", _udata=0x0, udata_size=0, buf=0x0, buf_size=0) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Lexternal.c:498
#1  0x000055555563f8f2 in H5G_link_to_info (lnk=0x555555b5d310, info=0x7fffffffcf60) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Glink.c:340
#2  0x000055555563e497 in H5G_visit_cb (lnk=0x555555b5d310, _udata=0x7fffffffd210) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:933
#3  0x000055555563fc26 in H5G__link_iterate_table (ltable=0x7fffffffd070, skip=0, last_lnk=0x0, op=0x55555563e2b5 <H5G_visit_cb>, op_data=0x7fffffffd210) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Glink.c:484
#4  0x000055555588df67 in H5G__compact_iterate (oloc=0x555555b5d178, dxpl_id=167772168, linfo=0x7fffffffd100, idx_type=H5_INDEX_NAME, order=H5_ITER_INC, skip=0, last_lnk=0x0, op=0x55555563e2b5 <H5G_visit_cb>, op_data=0x7fffffffd210) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:426
#5  0x0000555555649d46 in H5G__obj_iterate (grp_oloc=0x555555b5d178, idx_type=H5_INDEX_NAME, order=H5_ITER_INC, skip=0, last_lnk=0x0, op=0x55555563e2b5 <H5G_visit_cb>, op_data=0x7fffffffd210, dxpl_id=167772168) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:695
#6  0x000055555563f244 in H5G_visit (loc_id=16777216, group_name=0x5555558a85a0 "/", idx_type=H5_INDEX_NAME, order=H5_ITER_INC, op=0x5555555983d5 <traverse_cb>, op_data=0x7fffffffd340, lapl_id=167772160, dxpl_id=167772168) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172
#7  0x000055555583dc41 in H5Lvisit_by_name (loc_id=16777216, group_name=0x5555558a85a0 "/", idx_type=H5_INDEX_NAME, order=H5_ITER_INC, op=0x5555555983d5 <traverse_cb>, op_data=0x7fffffffd340, lapl_id=167772160) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376
#8  0x000055555559895e in traverse (file_id=16777216, grp_name=0x5555558a85a0 "/", visit_start=1, recurse=1, visitor=0x7fffffffd460) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289
#9  0x000055555559a0af in h5trav_visit (fid=16777216, grp_name=0x5555558a85a0 "/", visit_start=1, recurse=1, visit_obj=0x55555557eca1 <obj_stats>, visit_lnk=0x55555557ed6d <lnk_stats>, udata=0x7fffffffd4f0) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061
#10 0x0000555555580b50 in main (argc=2, argv=0x7fffffffd898) at /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5stat/h5stat.c:1618
#11 0x00007ffff7463b97 in __libc_start_main (main=0x555555580742 <main>, argc=2, argv=0x7fffffffd898, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffd888) at ../csu/libc-start.c:310
#12 0x000055555557dc4a in _start ()

src info:
493	    ssize_t     ret_value = SUCCEED;    /* Return value */
494	
495	    FUNC_ENTER_NOAPI_NOINIT
496	
497	    /* Check external link version & flags */
498	    if(((*udata >> 4) & 0x0F) != H5L_EXT_VERSION)
499	        HGOTO_ERROR(H5E_LINK, H5E_CANTDECODE, FAIL, "bad version number for external link")
500	    if((*udata & 0x0F) & ~H5L_EXT_FLAGS_ALL)
501	        HGOTO_ERROR(H5E_LINK, H5E_CANTDECODE, FAIL, "bad flags for external link")
502	

register info:
rax            0x0	0
rbx            0x0	0
rcx            0x0	0
rdx            0x0	0
rsi            0x0	0
rdi            0x555555b5d3d0	93824998560720
rbp            0x7fffffffce40	0x7fffffffce40
rsp            0x7fffffffcdf0	0x7fffffffcdf0
r8             0x0	0
r9             0x555555b5ca00	93824998558208
r10            0x7fffffffcea0	140737488342688
r11            0x7ffff75f1440	140737343591488
r12            0x55555557dc20	93824992402464
r13            0x7fffffffd890	140737488345232
r14            0x0	0
r15            0x0	0
rip            0x555555843d29	0x555555843d29 <H5L_extern_query+55>
eflags         0x10206	[ PF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0

```
## asan report
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==21969==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000ebbd3b bp 0x604000000d90 sp 0x7ffd026efa50 T0)
==21969==The signal is caused by a READ memory access.
==21969==Hint: address points to the zero page.
    #0 0xebbd3a in H5L_extern_query /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Lexternal.c:498:10
    #1 0x7800ed in H5G_link_to_info /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Glink.c:340:34
    #2 0x77e080 in H5G_visit_cb /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:933:8
    #3 0x7810ab in H5G__link_iterate_table /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Glink.c:484:21
    #4 0xf9927e in H5G__compact_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gcompact.c:426:21
    #5 0x79d8bd in H5G__obj_iterate /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gobj.c:695:29
    #6 0x77d172 in H5G_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Gint.c:1172:21
    #7 0xeae3ac in H5Lvisit_by_name /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5L.c:1376:21
    #8 0x57dba4 in traverse /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:289:16
    #9 0x581902 in h5trav_visit /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/lib/h5trav.c:1061:8
    #10 0x53595a in main /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/tools/h5stat/h5stat.c:1618:16
    #11 0x7f9f6fee2b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #12 0x43bed9 in _start (/home/pwd/fuzz/fuzz-hdf5/pwd-asan/installed/bin/h5stat+0x43bed9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/pwd/fuzz/fuzz-hdf5/hdf5-1.8.20/src/H5Lexternal.c:498:10 in H5L_extern_query
==21969==ABORTING

```


