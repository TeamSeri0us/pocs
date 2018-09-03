## Description

SoundTouch is an open-source audio processing library for changing the Tempo, Pitch and Playback Rates of audio streams or audio files. The library additionally supports estimating stable beats-per-minute rates for audio tracks.

## Version

[soundtouch](https://gitlab.com/soundtouch/soundtouch), 2.0.

## Others

this bug is reported by fish@360TeamSeri0us, 
please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details

1. 
Assertion failed in function main.cpp:232: void detectBPM(WavInFile*, RunParameters*): Assertion `BUFF_SIZE % nChannels == 0'.

```
root@50a1db6f0145:/work# ./soundstretch assertion-failed-1 /dev/null  -tempo=-50 -bpm=60 -pitch=-3 -rate=+35

   SoundStretch v2.1pre -  Copyright (c) Olli Parviainen
=========================================================
author e-mail: <oparviai@iki.fi> - WWW: http://www.surina.net/soundtouch

This program is subject to (L)GPL license. Run "soundstretch -license" for
more information.

Detecting BPM rate...soundstretch: main.cpp:232: void detectBPM(WavInFile*, RunParameters*): Assertion `BUFF_SIZE % nChannels == 0' failed.
Aborted (core dumped)

--------------------------------------------------------------------------------

root@50a1db6f0145:/work# gdb -q --args ./soundstretch assertion-failed-1-POC /dev/null  -tempo=-50 -bpm=60 -pitch=-3 -rate=+35
context = 'none'
clearscr = 'off'
Reading symbols from ./soundstretch...done.

Starting program: ./soundstretch assertion-failed-1-POC /dev/null -tempo=-50 -bpm=60 -pitch=-3 -rate=+35

   SoundStretch v2.1pre -  Copyright (c) Olli Parviainen
=========================================================
author e-mail: <oparviai@iki.fi> - WWW: http://www.surina.net/soundtouch

This program is subject to (L)GPL license. Run "soundstretch -license" for
more information.

Detecting BPM rate...soundstretch: main.cpp:232: void detectBPM(WavInFile*, RunParameters*): Assertion `BUFF_SIZE % nChannels == 0' failed.

Program received signal SIGABRT, Aborted.
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGABRT
0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
54	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
gdb-peda$ bt
#0  0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff727602a in __GI_abort () at abort.c:89
#2  0x00007ffff726cbd7 in __assert_fail_base (fmt=<optimized out>, assertion=assertion@entry=0x419143 "BUFF_SIZE % nChannels == 0", file=file@entry=0x41913a "main.cpp", line=line@entry=0xe8, function=function@entry=0x419380 <detectBPM(WavInFile*, RunParameters*)::__PRETTY_FUNCTION__> "void detectBPM(WavInFile*, RunParameters*)") at assert.c:92
#3  0x00007ffff726cc82 in __GI___assert_fail (assertion=assertion@entry=0x419143 "BUFF_SIZE % nChannels == 0", file=file@entry=0x41913a "main.cpp", line=line@entry=0xe8, function=function@entry=0x419380 <detectBPM(WavInFile*, RunParameters*)::__PRETTY_FUNCTION__> "void detectBPM(WavInFile*, RunParameters*)") at assert.c:101
#4  0x0000000000403a81 in detectBPM (inFile=inFile@entry=0x631ee0, params=0x631ea0, params=0x631ea0) at main.cpp:232
#5  0x0000000000402c24 in main (nParams=nParams@entry=0x7, paramStr=paramStr@entry=0x7fffffffe648) at main.cpp:295
#6  0x00007ffff725f830 in __libc_start_main (main=0x402970 <main(int, char const* const*)>, argc=0x7, argv=0x7fffffffe648, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe638) at ../csu/libc-start.c:291
#7  0x0000000000403589 in _start ()

```

2. Assertion failed in BPMDetect.cpp:190: soundtouch::BPMDetect::BPMDetect(int, int): Assertion `INPUT_BLOCK_SIZE < decimateBy * DECIMATED_BLOCK_SIZE' failed.

```

root@50a1db6f0145:/work# gdb -q --args ./soundstretch assertion-failed-2-POC /dev/null  -tempo=-50 -bpm=60 -pitch=-3 -rate=+35
context = 'none'
clearscr = 'off'
Reading symbols from ./soundstretch...done.
gdb-peda$ r
Starting program: ./soundstretch assertion-failed-2-POC /dev/null -tempo=-50 -bpm=60 -pitch=-3 -rate=+35

   SoundStretch v2.1pre -  Copyright (c) Olli Parviainen
=========================================================
author e-mail: <oparviai@iki.fi> - WWW: http://www.surina.net/soundtouch

This program is subject to (L)GPL license. Run "soundstretch -license" for
more information.

soundstretch: BPMDetect.cpp:190: soundtouch::BPMDetect::BPMDetect(int, int): Assertion `INPUT_BLOCK_SIZE < decimateBy * DECIMATED_BLOCK_SIZE' failed.

Program received signal SIGABRT, Aborted.
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGABRT
0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
54	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
gdb-peda$ bt
#0  0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff727602a in __GI_abort () at abort.c:89
#2  0x00007ffff726cbd7 in __assert_fail_base (fmt=<optimized out>, assertion=assertion@entry=0x7ffff7bd15e8 "INPUT_BLOCK_SIZE < decimateBy * DECIMATED_BLOCK_SIZE", file=file@entry=0x7ffff7bd15a0 "BPMDetect.cpp", line=line@entry=0xbe, function=function@entry=0x7ffff7bd17e0 <soundtouch::BPMDetect::BPMDetect(int, int)::__PRETTY_FUNCTION__> "soundtouch::BPMDetect::BPMDetect(int, int)") at assert.c:92
#3  0x00007ffff726cc82 in __GI___assert_fail (assertion=assertion@entry=0x7ffff7bd15e8 "INPUT_BLOCK_SIZE < decimateBy * DECIMATED_BLOCK_SIZE", file=file@entry=0x7ffff7bd15a0 "BPMDetect.cpp", line=line@entry=0xbe, function=function@entry=0x7ffff7bd17e0 <soundtouch::BPMDetect::BPMDetect(int, int)::__PRETTY_FUNCTION__> "soundtouch::BPMDetect::BPMDetect(int, int)") at assert.c:101
#4  0x00007ffff7bc038b in soundtouch::BPMDetect::BPMDetect (this=0x7fffffff7aa0, numChannels=0x1, aSampleRate=0x1e80) at BPMDetect.cpp:190
#5  0x00000000004036de in detectBPM (inFile=inFile@entry=0x631ee0, params=0x631ea0, params=0x631ea0) at main.cpp:224
#6  0x0000000000402c24 in main (nParams=nParams@entry=0x7, paramStr=paramStr@entry=0x7fffffffe648) at main.cpp:295
#7  0x00007ffff725f830 in __libc_start_main (main=0x402970 <main(int, char const* const*)>, argc=0x7, argv=0x7fffffffe648, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe638) at ../csu/libc-start.c:291
#8  0x0000000000403589 in _start ()


```

3.

```

root@50a1db6f0145:/work# gdb -q --args ./soundstretch POC-3 /dev/null -bpm=60
context = 'none'
clearscr = 'off'
Reading symbols from soundstretch...done.
gdb-peda$ r
Starting program: soundstretch crashes-2018-08-28-22-39/soundstretch001:id:000004,sig:06,src:001039,op:havoc,rep:8 /dev/null -bpm=60

   SoundStretch v2.1pre -  Copyright (c) Olli Parviainen
=========================================================
author e-mail: <oparviai@iki.fi> - WWW: http://www.surina.net/soundtouch

This program is subject to (L)GPL license. Run "soundstretch -license" for
more information.

Detecting BPM rate...Done!
Couldn't detect BPM rate.

Uses 32bit floating point sample type in processing.

Processing the file with the following changes:
  tempo change = +0 %
  pitch change = +0 semitones
  rate change  = +0 %

Working...*** Error in `soundstretch': corrupted size vs. prev_size: 0x000000000063ba70 ***

Program received signal SIGABRT, Aborted.
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGABRT
0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
54	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
gdb-peda$ bt
#0  0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff727602a in __GI_abort () at abort.c:89
#2  0x00007ffff72b67ea in __libc_message (do_abort=0x2, fmt=fmt@entry=0x7ffff73cfed8 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
#3  0x00007ffff72bfd36 in malloc_printerr (ar_ptr=0x7ffff7603b20 <main_arena>, ptr=<optimized out>, str=0x7ffff73ccc75 "corrupted size vs. prev_size", action=0x3) at malloc.c:5006
#4  _int_free (av=0x7ffff7603b20 <main_arena>, p=<optimized out>, have_lock=0x0) at malloc.c:4005
#5  0x00007ffff72c353c in __GI___libc_free (mem=<optimized out>) at malloc.c:2968
#6  0x0000000000407421 in WavFileBase::~WavFileBase (this=0x631ee0, __in_chrg=<optimized out>) at WavFile.cpp:148
#7  WavInFile::~WavInFile (this=0x631ee0, __in_chrg=<optimized out>) at WavFile.cpp:234
#8  WavInFile::~WavInFile (this=0x631ee0, __in_chrg=<optimized out>) at WavFile.cpp:238
#9  0x0000000000402ebd in main (nParams=nParams@entry=0x4, paramStr=paramStr@entry=0x7fffffffe678) at main.cpp:308
#10 0x00007ffff725f830 in __libc_start_main (main=0x402970 <main(int, char const* const*)>, argc=0x4, argv=0x7fffffffe678, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe668) at ../csu/libc-start.c:291
#11 0x0000000000403589 in _start ()


```

4. 

```
root@50a1db6f0145:/work# gdb -q --args ./soundstretch POC-00 /dev/null -tempo=-50
context = 'none'
clearscr = 'off'
Reading symbols from soundstretch...done.
gdb-peda$ r
Starting program: soundstretch POC-00 /dev/null -tempo=-50

   SoundStretch v2.1pre -  Copyright (c) Olli Parviainen
=========================================================
author e-mail: <oparviai@iki.fi> - WWW: http://www.surina.net/soundtouch

This program is subject to (L)GPL license. Run "soundstretch -license" for
more information.

Uses 32bit floating point sample type in processing.

Processing the file with the following changes:
  tempo change = -50 %
  pitch change = +0 semitones
  rate change  = +0 %

Working...*** Error in `soundstretch': double free or corruption (!prev): 0x00000000006323e0 ***

Program received signal SIGABRT, Aborted.
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGABRT
0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
54	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
gdb-peda$ bt
#0  0x00007ffff7274428 in __GI_raise (sig=sig@entry=0x6) at ../sysdeps/unix/sysv/linux/raise.c:54
#1  0x00007ffff727602a in __GI_abort () at abort.c:89
#2  0x00007ffff72b67ea in __libc_message (do_abort=do_abort@entry=0x2, fmt=fmt@entry=0x7ffff73cfed8 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
#3  0x00007ffff72bf37a in malloc_printerr (ar_ptr=<optimized out>, ptr=<optimized out>, str=0x7ffff73d0008 "double free or corruption (!prev)", action=0x3) at malloc.c:5006
#4  _int_free (av=<optimized out>, p=<optimized out>, have_lock=0x0) at malloc.c:3867
#5  0x00007ffff72c353c in __GI___libc_free (mem=<optimized out>) at malloc.c:2968
#6  0x0000000000407741 in WavFileBase::~WavFileBase (this=0x631f50, __in_chrg=<optimized out>) at WavFile.cpp:148
#7  WavOutFile::~WavOutFile (this=0x631f50, __in_chrg=<optimized out>) at WavFile.cpp:739
#8  WavOutFile::~WavOutFile (this=0x631f50, __in_chrg=<optimized out>) at WavFile.cpp:744
#9  0x0000000000402f06 in main (nParams=nParams@entry=0x4, paramStr=paramStr@entry=0x7fffffffe6b8) at main.cpp:309
#10 0x00007ffff725f830 in __libc_start_main (main=0x402970 <main(int, char const* const*)>, argc=0x4, argv=0x7fffffffe6b8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe6a8) at ../csu/libc-start.c:291
#11 0x0000000000403589 in _start ()

```
