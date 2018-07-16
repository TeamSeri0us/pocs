## Description

FAAC is an Advanced Audio Coder (MPEG2-AAC, MPEG4-AAC). The goal of FAAC is to explore the possibilities of AAC and exceed the quality of the currently best MP3 encoders.


## Version
faac, 2.1.

## Others
this bug is reported by fish@360TeamSeri0us, please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details
A divide by zero error can be found  in pcmfile_t *wav_open_read(const char *name, int rawinput)
 in input.c, this could result in denial of service.
 
 
```c
pcmfile_t *wav_open_read(const char *name, int rawinput)
{
  FILE *wave_f;
  riff_t riff;
  riffsub_t riffsub;
  struct WAVEFORMATEXTENSIBLE wave;
  char *riffl = "RIFF";
  char *wavel = "WAVE";
  char *fmtl = "fmt ";
  char *datal = "data";
  int fmtsize;
  pcmfile_t *sndf;
  int dostdin = 0;

  if (!strcmp(name, "-"))
  {
#ifdef _WIN32
    _setmode(_fileno(stdin), O_BINARY);
#endif
    wave_f = stdin;
    dostdin = 1;
  }
  else if (!(wave_f = fopen(name, "rb")))
  {
    perror(name);
    return NULL;
  }

  if (!rawinput) // header input
  {
    if (fread(&riff, 1, sizeof(riff), wave_f) != sizeof(riff))
      return NULL;
    if (memcmp(&(riff.label), riffl, 4))
      return NULL;
    if (memcmp(&(riff.chunk_type), wavel, 4))
      return NULL;

    if (!seekchunk(wave_f, &riffsub, fmtl))
      return NULL;

    if (memcmp(&(riffsub.label), fmtl, 4))
        return NULL;
    memset(&wave, 0, sizeof(wave));

    fmtsize = (riffsub.len < sizeof(wave)) ? riffsub.len : sizeof(wave);
    // check if format is at least 16 bytes long
    if (fmtsize < 16)
	return NULL;

   if (fread(&wave, 1, fmtsize, wave_f) != fmtsize)
        return NULL;

    seekcur(wave_f, riffsub.len - fmtsize);

    if (!seekchunk(wave_f, &riffsub, datal))
      return NULL;

    if (UINT16(wave.Format.wFormatTag) != WAVE_FORMAT_PCM && UINT16(wave.Format.wFormatTag) != WAVE_FORMAT_FLOAT)
    {
      if (UINT16(wave.Format.wFormatTag) == WAVE_FORMAT_EXTENSIBLE)
      {
        if (UINT16(wave.Format.cbSize) < 22) // struct too small
          return NULL;
        if (memcmp(wave.SubFormat, waveformat_pcm_guid, 16))
        {
          waveformat_pcm_guid[0] = WAVE_FORMAT_FLOAT;
          if (memcmp(wave.SubFormat, waveformat_pcm_guid, 16))
          {          
            unsuperr(name);
            return NULL;
          }
        }
      }
      else
      {
        unsuperr(name);
        return NULL;
      }
    }
  }

  sndf = malloc(sizeof(*sndf));
  memset(sndf, 0, sizeof(*sndf));
  sndf->f = wave_f;

  if (UINT16(wave.Format.wFormatTag) == WAVE_FORMAT_FLOAT) {
    sndf->isfloat = 1;
  } else {
    sndf->isfloat = (wave.SubFormat[0] == WAVE_FORMAT_FLOAT);
  }
  if (rawinput)
  {
    sndf->bigendian = 1;
    if (dostdin)
      sndf->samples = 0;
    else
    {
      fseek(sndf->f, 0 , SEEK_END);
      sndf->samples = ftell(sndf->f);
      rewind(sndf->f);
    }
  }
  else
  {
    sndf->bigendian = 0;
    sndf->channels = UINT16(wave.Format.nChannels);
    sndf->samplebytes = UINT16(wave.Format.wBitsPerSample) / 8;
    sndf->samplerate = UINT32(wave.Format.nSamplesPerSec);
    sndf->samples = riffsub.len / (sndf->samplebytes * sndf->channels);
  }
  return sndf;
}

```
