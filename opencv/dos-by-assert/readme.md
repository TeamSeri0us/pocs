DOS by assert in opencv library
==================

## 1. opencv-assert-dos-1

```
Starting program: /work/test-driver/opencv_test.elf ../crashes/dos-1
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
OpenCV(3.4.1-dev) Error: Assertion failed (pixels <= (1<<30)) in validateInputImageSize, file /src/opencv/modules/imgcodecs/src/loadsave.cpp, line 74
terminate called after throwing an instance of 'cv::Exception'
  what():  OpenCV(3.4.1-dev) /src/opencv/modules/imgcodecs/src/loadsave.cpp:74: error: (-215) pixels <= (1<<30) in function validateInputImageSize


Program received signal SIGABRT, Aborted.
0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
54      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff1d5402a in __GI_abort () at abort.c:89
#2  0x00007ffff238c84d in __gnu_cxx::__verbose_terminate_handler() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff238a6b6 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007ffff238a701 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#5  0x00007ffff238a919 in __cxa_throw () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#6  0x00007ffff27ef928 in cv::error (exc=...) at /src/opencv/modules/core/src/system.cpp:914
#7  0x00007ffff27efcc1 in cv::error (_code=_code@entry=-215, _err=..., _func=_func@entry=0x7ffff7875b30 <cv::validateInputImageSize(cv::Size_<int> const&)::__func__> "validateInputImageSize",
    _file=_file@entry=0x7ffff7875818 "/src/opencv/modules/imgcodecs/src/loadsave.cpp", _line=_line@entry=74) at /src/opencv/modules/core/src/system.cpp:919
#8  0x00007ffff7228af1 in cv::validateInputImageSize (size=...) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:74
#9  0x00007ffff722dd1b in cv::imread_ (filename=..., flags=flags@entry=1, hdrtype=hdrtype@entry=2, mat=mat@entry=0x7fffffffe4a0) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:451
#10 0x00007ffff72302bd in cv::imread (filename=..., flags=1) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:641
#11 0x0000000000400e69 in main ()
```

## 2. opencv-assert-dos-2

```
Starting program: /work/test-driver/opencv_test.elf ../crashes/dos-2
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
OpenCV(3.4.1-dev) Error: Assertion failed (size.width <= (1<<20)) in validateInputImageSize, file /src/opencv/modules/imgcodecs/src/loadsave.cpp, line 70
terminate called after throwing an instance of 'cv::Exception'
  what():  OpenCV(3.4.1-dev) /src/opencv/modules/imgcodecs/src/loadsave.cpp:70: error: (-215) size.width <= (1<<20) in function validateInputImageSize


Program received signal SIGABRT, Aborted.
0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
54      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff1d5402a in __GI_abort () at abort.c:89
#2  0x00007ffff238c84d in __gnu_cxx::__verbose_terminate_handler() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff238a6b6 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007ffff238a701 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#5  0x00007ffff238a919 in __cxa_throw () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#6  0x00007ffff27ef928 in cv::error (exc=...) at /src/opencv/modules/core/src/system.cpp:914
#7  0x00007ffff27efcc1 in cv::error (_code=_code@entry=-215, _err=..., _func=_func@entry=0x7ffff7875b30 <cv::validateInputImageSize(cv::Size_<int> const&)::__func__> "validateInputImageSize",
    _file=_file@entry=0x7ffff7875818 "/src/opencv/modules/imgcodecs/src/loadsave.cpp", _line=_line@entry=70) at /src/opencv/modules/core/src/system.cpp:919
#8  0x00007ffff7228bf0 in cv::validateInputImageSize (size=...) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:70
#9  0x00007ffff722dd1b in cv::imread_ (filename=..., flags=flags@entry=1, hdrtype=hdrtype@entry=2, mat=mat@entry=0x7fffffffe4a0) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:451
#10 0x00007ffff72302bd in cv::imread (filename=..., flags=1) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:641
#11 0x0000000000400e69 in main ()


```





## 3. opencv-assert-dos-3

```
Starting program: /work/test-driver/opencv_test.elf ../crashes/dos-3
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
OpenCV(3.4.1-dev) Error: Assertion failed (size.height <= (1<<20)) in validateInputImageSize, file /src/opencv/modules/imgcodecs/src/loadsave.cpp, line 72
terminate called after throwing an instance of 'cv::Exception'
  what():  OpenCV(3.4.1-dev) /src/opencv/modules/imgcodecs/src/loadsave.cpp:72: error: (-215) size.height <= (1<<20) in function validateInputImageSize


Program received signal SIGABRT, Aborted.
0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
54      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  0x00007ffff1d52428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff1d5402a in __GI_abort () at abort.c:89
#2  0x00007ffff238c84d in __gnu_cxx::__verbose_terminate_handler() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff238a6b6 in ?? () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007ffff238a701 in std::terminate() () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#5  0x00007ffff238a919 in __cxa_throw () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#6  0x00007ffff27ef928 in cv::error (exc=...) at /src/opencv/modules/core/src/system.cpp:914
#7  0x00007ffff27efcc1 in cv::error (_code=_code@entry=-215, _err=..., _func=_func@entry=0x7ffff7875b30 <cv::validateInputImageSize(cv::Size_<int> const&)::__func__> "validateInputImageSize",
    _file=_file@entry=0x7ffff7875818 "/src/opencv/modules/imgcodecs/src/loadsave.cpp", _line=_line@entry=72) at /src/opencv/modules/core/src/system.cpp:919
#8  0x00007ffff7228b75 in cv::validateInputImageSize (size=...) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:72
#9  0x00007ffff722dd1b in cv::imread_ (filename=..., flags=flags@entry=1, hdrtype=hdrtype@entry=2, mat=mat@entry=0x7fffffffe4a0) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:451
#10 0x00007ffff72302bd in cv::imread (filename=..., flags=1) at /src/opencv/modules/imgcodecs/src/loadsave.cpp:641
#11 0x0000000000400e69 in main ()


```




