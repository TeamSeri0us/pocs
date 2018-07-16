## Description

FAAC is an Advanced Audio Coder (MPEG2-AAC, MPEG4-AAC). The goal of FAAC is to explore the possibilities of AAC and exceed the quality of the currently best MP3 encoders.


## Version
faac, 2.1.

## Others
this bug is reported by fish@360TeamSeri0us, please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details
A divide by zero error can be found  in pcmfile_t *wav_open_read(const char *name, int rawinput)
 in input.c, this could result in denial of service.
 
 
