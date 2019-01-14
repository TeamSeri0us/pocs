
## target 

GNU Recutils is a set of tools and libraries to access human-editable, plain text databases called recfiles. The data is stored as a sequence of records, each record containing an arbitrary number of named fields. The picture below shows a sample database containing information about GNU packages, along with the main features provided by recutils.


## version

 [1.8](https://ftp.gnu.org/gnu/recutils/)

## others

This bug is reported by fish@360TeamSeri0us, please send email to teamSeri0us360@gmail.com if you have any question.

## details 



1. There is a double-free problem in function rec_mset_elem_destroy() in file src/rec-mset.c.


fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ ./debug/bin/rec2csv data/double-free-poc-1  
double free or corruption (fasttop)
Aborted (core dumped)

### asan report

```
=================================================================
==6397==ERROR: AddressSanitizer: attempting double-free on 0x602000009df0 in thread T0:
    #0 0x4cdb78 in __interceptor_free.localalias.0 (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdb78)
    #1 0x7f31ac47c7c0 in rec_mset_elem_destroy /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:905:11
    #2 0x7f31ac47c7c0 in rec_mset_elem_dispose_fn /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:814
    #3 0x7f31ac4eb213 in gl_array_list_free /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:436:17
    #4 0x7f31ac47ca18 in gl_list_free /home/fish/Desktop/dumb/archive/recutils-1.8/src/../lib/gl_list.h:760:3
    #5 0x7f31ac47ca18 in rec_mset_destroy /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:152
    #6 0x7f31ac48cb9a in rec_rset_destroy /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:263:7
    #7 0x7f31ac4a6208 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:612:7
    #8 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #9 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20
    #10 0x509204 in main /home/fish/Desktop/dumb/archive/recutils-1.8/utils/rec2csv.c:342:8
    #11 0x7f31ab314b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #12 0x41e759 in _start (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x41e759)

0x602000009df0 is located 0 bytes inside of 16-byte region [0x602000009df0,0x602000009e00)
freed by thread T0 here:
    #0 0x4cdb78 in __interceptor_free.localalias.0 (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdb78)
    #1 0x7f31ac47c7c0 in rec_mset_elem_destroy /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:905:11
    #2 0x7f31ac47c7c0 in rec_mset_elem_dispose_fn /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:814

previously allocated by thread T0 here:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7f31ac485c79 in rec_comment_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-comment.c:43:10
    #2 0x7f31ac4a5fd2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:549:11
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

SUMMARY: AddressSanitizer: double-free (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdb78) in __interceptor_free.localalias.0
==6397==ABORTING

```


### gdb debug info

```
fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ gdb -q --args ./debug/bin/rec2csv data/double-free-poc-1 

gef➤  bt
#0  __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff727a801 in __GI_abort () at abort.c:79
#2  0x00007ffff72c3897 in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff73f0b9a "%s\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff72ca90a in malloc_printerr (str=str@entry=0x7ffff73f2828 "double free or corruption (fasttop)") at malloc.c:5350
#4  0x00007ffff72d2004 in _int_free (have_lock=0x0, p=0x55555577c300, av=0x7ffff7625c40 <main_arena>) at malloc.c:4230
#5  __GI___libc_free (mem=0x55555577c310) at malloc.c:3124
#6  0x00007ffff7b76792 in rec_comment_destroy (comment=0x55555577c310 " \302wUUU") at rec-comment.c:49
#7  0x00007ffff7b79e51 in rec_rset_comment_disp_fn (data=0x55555577c310) at rec-rset.c:1031
#8  0x00007ffff7b75a93 in rec_mset_elem_destroy (elem=0x55555579ca30) at rec-mset.c:905
#9  0x00007ffff7b75844 in rec_mset_elem_dispose_fn (e=0x55555579ca30) at rec-mset.c:814
#10 0x00007ffff7b92fc0 in gl_array_list_free (list=0x55555579aec0) at gl_array_list.c:436
#11 0x00007ffff7b958f9 in gl_list_free (list=0x55555579aec0) at gl_list.h:760
#12 0x00007ffff7b74381 in rec_mset_destroy (mset=0x55555579ade0) at rec-mset.c:152
#13 0x00007ffff7b78b4d in rec_rset_destroy (rset=0x55555579ad80) at rec-rset.c:263
#14 0x00007ffff7b7eca5 in rec_parse_rset (parser=0x55555579ad30, rset=0x7fffffffdbc0) at rec-parser.c:612
#15 0x00005555555586cf in recutl_parse_db_from_file (in=0x555555798330, file_name=0x7fffffffe19d "data/double-free-poc-1", db=0x55555577bc30) at recutl.c:246
#16 0x00005555555587fc in recutl_build_db (argc=0x2, argv=0x7fffffffdda8) at recutl.c:332
#17 0x000055555555996d in main (argc=0x2, argv=0x7fffffffdda8) at rec2csv.c:342

```


2. There is a null-pointer-dereference problem in function rec_fex_size() in file src/rec-fex.c.

fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ ./debug/bin/rec2csv data/null-pointer-dereference-poc-2
Segmentation fault (core dumped)

### asan report 

```
ASAN:DEADLYSIGNAL
=================================================================
==6373==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fef5bfd18d2 bp 0x7ffddef54bf0 sp 0x7ffddef54890 T0)
==6373==The signal is caused by a READ memory access.
==6373==Hint: address points to the zero page.
    #0 0x7fef5bfd18d1 in rec_fex_size /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-fex.c:257:15
    #1 0x7fef5bf89df4 in rec_rset_update_field_props /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:1243:31
    #2 0x7fef5bf88b85 in rec_rset_set_descriptor /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:354:3
    #3 0x7fef5bfa0f02 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:578:23
    #4 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #5 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20
    #6 0x509204 in main /home/fish/Desktop/dumb/archive/recutils-1.8/utils/rec2csv.c:342:8
    #7 0x7fef5ae0fb96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #8 0x41e759 in _start (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x41e759)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-fex.c:257:15 in rec_fex_size
==6373==ABORTING

```


### gdb debug info

```
fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ gdb -q --args ./debug/bin/rec2csv data/null-pointer-dereference-poc-2

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ source:rec-fex.c+257 ]────
    252	 }
    253	 
    254	 size_t
    255	 rec_fex_size (rec_fex_t fex)
    256	 {
 →  257	   return fex->num_elems;
    258	 }
    259	 
    260	 rec_fex_elem_t
    261	 rec_fex_get (rec_fex_t fex,
    262	              size_t position)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ threads ]────
[#0] Id 1, Name: "rec2csv", stopped, reason: SIGSEGV
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ trace ]────
[#0] 0x7ffff7b8d46b → Name: rec_fex_size(fex=0x0)
[#1] 0x7ffff7b7a5fb → Name: rec_rset_update_field_props(rset=0x55555579ade0)
[#2] 0x7ffff7b78d83 → Name: rec_rset_set_descriptor(rset=0x55555579ade0, record=0x55555579cb90)
[#3] 0x7ffff7b7ebce → Name: rec_parse_rset(parser=0x55555579ad30, rset=0x7fffffffdb80)
[#4] 0x5555555586cf → Name: recutl_parse_db_from_file(in=0x555555798330, file_name=0x7fffffffe15d "data/null-pointer-dereference-poc-2", db=0x55555577bc30)
[#5] 0x5555555587fc → Name: recutl_build_db(argc=0x2, argv=0x7fffffffdd68)
[#6] 0x55555555996d → Name: main(argc=0x2, argv=0x7fffffffdd68)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
0x00007ffff7b8d46b in rec_fex_size (fex=0x0) at rec-fex.c:257
257	  return fex->num_elems;
gef➤  bt
#0  0x00007ffff7b8d46b in rec_fex_size (fex=0x0) at rec-fex.c:257
#1  0x00007ffff7b7a5fb in rec_rset_update_field_props (rset=0x55555579ade0) at rec-rset.c:1243
#2  0x00007ffff7b78d83 in rec_rset_set_descriptor (rset=0x55555579ade0, record=0x55555579cb90) at rec-rset.c:354
#3  0x00007ffff7b7ebce in rec_parse_rset (parser=0x55555579ad30, rset=0x7fffffffdb80) at rec-parser.c:578
#4  0x00005555555586cf in recutl_parse_db_from_file (in=0x555555798330, file_name=0x7fffffffe15d "data/null-pointer-dereference-poc-2", db=0x55555577bc30) at recutl.c:246
#5  0x00005555555587fc in recutl_build_db (argc=0x2, argv=0x7fffffffdd68) at recutl.c:332
#6  0x000055555555996d in main (argc=0x2, argv=0x7fffffffdd68) at rec2csv.c:342
gef➤  p *fex
Cannot access memory at address 0x0
```

3. There are multiple memory leak problems in recutils-1.8.

```

fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ ASAN_OPTIONS=detect_odr_violation=0 ./fast/bin/rec2csv  data/memory-leak-poc-3 
data/memory-leak-poc-3: 56: error: expected a record

=================================================================
==8363==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 648 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2c160a in rec_aggregate_reg_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-aggregate.c:117:9
    #2 0x7fbaf90f5b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310

Direct leak of 64 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2c79e7 in gl_array_nx_create_empty /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:60:29

Direct leak of 40 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2c0be5 in rec_buf_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-buf.c:55:9
    #2 0x7fbafa286fd2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:549:11
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Direct leak of 5 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa264522 in rec_extract_type /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-utils.c:159:18
    #2 0x7fbafa272263 in rec_rset_type /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:420:17
    #3 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 624 byte(s) in 3 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa25cf82 in rec_mset_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:109:9
    #2 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 512 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2c0c5a in rec_buf_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-buf.c:61:19
    #2 0x7fbafa286fd2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:549:11
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 256 byte(s) in 4 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2c79e7 in gl_array_nx_create_empty /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:60:29

Indirect leak of 208 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa25cf82 in rec_mset_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:109:9
    #2 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #3 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 192 byte(s) in 6 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa260c6a in rec_mset_elem_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:882:9
    #2 0x7fbafa260c6a in rec_mset_insert_at /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:434

Indirect leak of 192 byte(s) in 3 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa268752 in rec_record_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-record.c:81:12
    #2 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 192 byte(s) in 3 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2675a7 in rec_field_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:103:11
    #2 0x7fbafa283dbd in rec_parse_record /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:436:7
    #3 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #4 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #5 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 88 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa26d490 in rec_rset_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:169:10
    #2 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #3 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 69 byte(s) in 3 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa26b52c in rec_record_set_source /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-record.c:497:20
    #2 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 69 byte(s) in 3 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa26829b in rec_field_set_source /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:236:19
    #2 0x7fbafa283dbd in rec_parse_record /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:436:7
    #3 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #4 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #5 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 57 byte(s) in 8 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa25f867 in rec_mset_register_type /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-mset.c:303:26

Indirect leak of 48 byte(s) in 4 object(s) allocated from:
    #0 0x4ce155 in realloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4ce155)
    #1 0x7fbafa2c9430 in grow /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:261:28
    #2 0x7fbafa2c9430 in gl_array_nx_add_last /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:294

Indirect leak of 43 byte(s) in 3 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa26766b in rec_field_set_value /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:93:18
    #2 0x7fbafa26766b in rec_field_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:116

Indirect leak of 30 byte(s) in 12 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbaf915c61f in vasprintf /build/glibc-OTsEL5/glibc-2.27/libio/vasprintf.c:73

Indirect leak of 22 byte(s) in 5 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa2c1f74 in rec_aggregate_reg_add /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-aggregate.c:162:59
    #2 0x7fbafa2c1f74 in rec_aggregate_reg_add_standard /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-aggregate.c:193

Indirect leak of 16 byte(s) in 1 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa266c79 in rec_comment_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-comment.c:43:10
    #2 0x7fbafa286fd2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:549:11
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 16 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa2be0ba in rec_type_reg_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-types.c:707:9
    #2 0x7fbafa286f02 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:578:23
    #3 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #4 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 14 byte(s) in 3 object(s) allocated from:
    #0 0x46e820 in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x46e820)
    #1 0x7fbafa2675f4 in rec_field_set_name /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:78:17
    #2 0x7fbafa2675f4 in rec_field_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:109
    #3 0x7fbafa283dbd in rec_parse_record /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:436:7
    #4 0x7fbafa286de2 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:560:15
    #5 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #6 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

Indirect leak of 8 byte(s) in 1 object(s) allocated from:
    #0 0x4ce155 in realloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4ce155)
    #1 0x7fbafa2c8d42 in grow /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:261:28
    #2 0x7fbafa2c8d42 in gl_array_nx_add_first /home/fish/Desktop/dumb/archive/recutils-1.8/lib/gl_array_list.c:278

Indirect leak of 1 byte(s) in 1 object(s) allocated from:
    #0 0x4cdd30 in __interceptor_malloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/rec2csv+0x4cdd30)
    #1 0x7fbafa26f05c in rec_rset_update_sex_constraints /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:1091:25
    #2 0x7fbafa26f05c in rec_rset_set_descriptor /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-rset.c:356
    #3 0x7fbafa286f02 in rec_parse_rset /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-parser.c:578:23
    #4 0x506d81 in recutl_parse_db_from_file /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:246:10
    #5 0x5073fe in recutl_build_db /home/fish/Desktop/dumb/archive/recutils-1.8/utils/recutl.c:332:20

SUMMARY: AddressSanitizer: 3414 byte(s) leaked in 71 allocation(s).


```

4. There is a null-pointer-dereference problem in function rec_field_set_name() in file src/rec-field.c.

fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ ./debug/bin/rec2csv data/null-pointer-dereference-poc-4
Segmentation fault (core dumped)

### asan report 

```
ASAN:DEADLYSIGNAL
=================================================================
==8402==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f8ad54655c7 bp 0x7fff9c74b850 sp 0x7fff9c74afd8 T0)
==8402==The signal is caused by a READ memory access.
==8402==Hint: address points to the zero page.
    #0 0x7f8ad54655c6  /build/glibc-OTsEL5/glibc-2.27/string/../sysdeps/x86_64/multiarch/strlen-avx2.S:92
    #1 0x46e36f in strdup (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/csv2rec+0x46e36f)
    #2 0x7f8ad646a5f4 in rec_field_set_name /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:78:17
    #3 0x7f8ad646a5f4 in rec_field_new /home/fish/Desktop/dumb/archive/recutils-1.8/src/rec-field.c:109
    #4 0x509aa5 in field_cb /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:264:19
    #5 0x57571d in csv_parse /home/fish/Desktop/dumb/archive/recutils-1.8/libcsv/libcsv.c:395:13
    #6 0x5090a6 in process_csv /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:374:11
    #7 0x5090a6 in main /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:395
    #8 0x7f8ad52f8b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #9 0x41e3e9 in _start (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/csv2rec+0x41e3e9)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /build/glibc-OTsEL5/glibc-2.27/string/../sysdeps/x86_64/multiarch/strlen-avx2.S:92 
==8402==ABORTING

```

### gdb debug info 

```
gef➤  bt
#0  __strlen_avx2 () at ../sysdeps/x86_64/multiarch/strlen-avx2.S:62
#1  0x00007ffff72d79ae in __GI___strdup (s=0x0) at strdup.c:41
#2  0x00007ffff7b76a12 in rec_field_set_name (field=0x5555557a1a50, name=0x0) at rec-field.c:78
#3  0x00007ffff7b76ac8 in rec_field_new (name=0x0, value=0x55555577db10 "e\350\003\"\"") at rec-field.c:109
#4  0x0000555555559195 in field_cb (s=0x55555579ba60, len=0x5, data=0x7fffffffd790) at csv2rec.c:264
#5  0x0000555555573a09 in csv_parse (p=0x7fffffffd7d0, s=0x7fffffffd830, len=0x9a, cb1=0x555555558f2c <field_cb>, cb2=0x5555555591e2 <record_cb>, data=0x7fffffffd790) at libcsv.c:395
#6  0x00005555555594ce in process_csv () at csv2rec.c:374
#7  0x000055555555959a in main (argc=0x2, argv=0x7fffffffdd78) at csv2rec.c:395

gef➤  p field->name
$1 = 0x0

```



5. There is a heap-buffer-overflow problem in function field_cb() in file utils/csv2rec.c.

fish@ubuntu:~/Desktop/dumb/archive/recutils-1.8$ ./debug/bin/csv2rec  data/heap-buffer-overflow-poc-5 
Segmentation fault (core dumped)
### asan report

```
=================================================================
==8780==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001f280 at pc 0x000000509c79 bp 0x7ffdc361ebd0 sp 0x7ffdc361ebc8
READ of size 8 at 0x61d00001f280 thread T0
    #0 0x509c78 in field_cb /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:264:34
    #1 0x57521e in csv_parse /home/fish/Desktop/dumb/archive/recutils-1.8/libcsv/libcsv.c:361:11
    #2 0x5090a6 in process_csv /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:374:11
    #3 0x5090a6 in main /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:395
    #4 0x7ff3e2d38b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #5 0x41e3e9 in _start (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/csv2rec+0x41e3e9)

0x61d00001f280 is located 0 bytes to the right of 2048-byte region [0x61d00001ea80,0x61d00001f280)
allocated by thread T0 here:
    #0 0x4cdde5 in realloc (/home/fish/Desktop/dumb/archive/recutils-1.8/fast/bin/csv2rec+0x4cdde5)
    #1 0x509608 in field_cb /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:214:11

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/fish/Desktop/dumb/archive/recutils-1.8/utils/csv2rec.c:264:34 in field_cb
Shadow bytes around the buggy address:
  0x0c3a7fffbe00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbe10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbe20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbe30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbe40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fffbe50:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbe60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbe70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbe80: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbe90: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbea0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==8780==ABORTING

```

