## Description
The PoDoFo library is a free, portable C++ library. It can parse and modify existing PDF files and create new ones from scratch. It also includes several tools to work with PDF files.
link: https://sourceforge.net/projects/podofo/

An issuse was discovered in PoDoFo 0.9.6. There is a reachable abort at PoDoFo:podofo_calloc, due to a big memory calloc, leads to a Denial of Service.

## version
PoDoFo Version: 0.9.6

## others
this bug is reported by pwd@360TeamSeri0us, 
please send email to  teamSeri0us360@gmail.com if you have any questions.

## Target

```shell
./podofocrop  ~/newpocs/podofo/crop/callocFailed-podofo_calloc.pdf out.pdf
```

## ASAN report
```txt
Cropping file:	/home/pwd/newpocs/podofo/crop/callocFailed-podofo_calloc
Writing to   :	out.pdf
==93472==WARNING: AddressSanitizer failed to allocate 0xfffffffffffffff2 bytes
==93472==AddressSanitizer's allocator is terminating the process instead of returning 0
==93472==If you don't like this behavior set allocator_may_return_null=1
==93472==AddressSanitizer CHECK failed: /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/sanitizer_common/sanitizer_allocator.cc:225 "((0)) != (0)" (0x0, 0x0)
    #0 0x527ca5 in __asan::AsanCheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_rtl.cc:69
    #1 0x545555 in __sanitizer::CheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/sanitizer_common/sanitizer_termination.cc:79
    #2 0x52e096 in __sanitizer::ReportAllocatorCannotReturnNull() /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/sanitizer_common/sanitizer_allocator.cc:225
    #3 0x52e0d6 in __sanitizer::ReturnNullOrDieOnFailure::OnBadRequest() /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/sanitizer_common/sanitizer_allocator.cc:241
    #4 0x469cb9 in __asan::Allocator::Calloc(unsigned long, unsigned long, __sanitizer::BufferedStackTrace*) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_allocator.cc:665
    #5 0x469cb9 in __asan::asan_calloc(unsigned long, unsigned long, __sanitizer::BufferedStackTrace*) /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_allocator.cc:860
    #6 0x51ed52 in calloc /home/pwd/llvm_dev/llvm/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:98
    #7 0x77870c in PoDoFo::podofo_calloc(unsigned long, unsigned long) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfMemoryManagement.cpp:136:9
    #8 0x7664c5 in PoDoFo::PdfPredictorDecoder::PdfPredictorDecoder(PoDoFo::PdfDictionary const*) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfFiltersPrivate.cpp:112:38
    #9 0x75c9e1 in PoDoFo::PdfFlateFilter::BeginDecodeImpl(PoDoFo::PdfDictionary const*) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfFiltersPrivate.cpp:560:39
    #10 0x755648 in PoDoFo::PdfFilter::BeginDecode(PoDoFo::PdfOutputStream*, PoDoFo::PdfDictionary const*) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfFilter.h:380:3
    #11 0x757105 in PoDoFo::PdfFilteredDecodeStream::PdfFilteredDecodeStream(PoDoFo::PdfOutputStream*, PoDoFo::EPdfFilter, bool, PoDoFo::PdfDictionary const*) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfFilter.cpp:169:19
    #12 0x74fa77 in PoDoFo::PdfFilterFactory::CreateDecodeStream(std::vector<PoDoFo::EPdfFilter, std::allocator<PoDoFo::EPdfFilter> > const&, PoDoFo::PdfOutputStream*, PoDoFo::PdfDictionary const*) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfFilter.cpp:351:44
    #13 0x5931da in PoDoFo::PdfStream::GetFilteredCopy(char**, long*) const /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfStream.cpp:96:55
    #14 0x7f9d6d in PoDoFo::PdfXRefStreamParserObject::ParseStream(long const*, std::vector<long, std::allocator<long> > const&) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfXRefStreamParserObject.cpp:146:24
    #15 0x7f5d54 in PoDoFo::PdfXRefStreamParserObject::ReadXRefTable() /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfXRefStreamParserObject.cpp:118:5
    #16 0x79524f in PoDoFo::PdfParser::ReadXRefStreamContents(long, bool) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfParser.cpp:947:16
    #17 0x786a13 in PoDoFo::PdfParser::ReadXRefContents(long, bool) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfParser.cpp:727:13
    #18 0x77fe8f in PoDoFo::PdfParser::ReadDocumentStructure() /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfParser.cpp:373:9
    #19 0x77d9c0 in PoDoFo::PdfParser::ParseFile(PoDoFo::PdfRefCountedInputDevice const&, bool) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfParser.cpp:259:9
    #20 0x77bba4 in PoDoFo::PdfParser::ParseFile(char const*, bool) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/base/PdfParser.cpp:206:11
    #21 0x657abb in PoDoFo::PdfMemDocument::Load(char const*, bool) /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/src/doc/PdfMemDocument.cpp:256:16
    #22 0x55dcf5 in main /home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/tools/podofocrop/podofocrop.cpp:214:13
    #23 0x7f5e35e77b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #24 0x45ec99 in _start (/home/pwd/fuzz/from_exploit/podofo/podofo-0.9.6/pwd-installed/bin/podofocrop+0x45ec99)
```

## Debug infomation

In line 136, function PoDoFo::podofo_calloc, it doesn`t check out calloced size before it call the funcion 'calloc'.

```c
    129		if ((nmemb >= MUL_NO_OVERFLOW || size >= MUL_NO_OVERFLOW) &&
    130	 		nmemb > 0 && SIZE_MAX / nmemb < size)
    131	 	{
    132	 		errno = ENOMEM;
    133	 		return NULL;
    134	 	}
    135	 
 →  136	 	return calloc(nmemb, size);
    137	 }
    138	 
    139	 void* podofo_realloc( void* buffer, size_t size )
    140	 {
    141	 	/*
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "podofocrop", stopped, reason: SINGLE STEP
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x779c2c → PoDoFo::podofo_calloc(nmemb=0xfffffffffffffff2, size=0x1)
[#1] 0x767976 → PoDoFo::PdfPredictorDecoder::PdfPredictorDecoder(this=0x604000001e50, pDecodeParms=0x6070000028d0)
[#2] 0x75cf12 → PoDoFo::PdfFlateFilter::BeginDecodeImpl(this=0x621000005100, pDecodeParms=0x6070000028d0)
[#3] 0x755b79 → PoDoFo::PdfFilter::BeginDecode(this=0x621000005100, pOutput=0x7fffffffc590, pDecodeParms=0x6070000028d0)
[#4] 0x757636 → PoDoFo::PdfFilteredDecodeStream::PdfFilteredDecodeStream(this=<optimized out>, pOutputStream=0x7fffffffc590, eFilter=<optimized out>, bOwnStream=0x0, pDecodeParms=0x6070000028d0)
[#5] 0x74ffa8 → PoDoFo::PdfFilterFactory::CreateDecodeStream(filters=<optimized out>, pStream=0x7fffffffc590, pDictionary=0x6070000028d0)
[#6] 0x59368b → PoDoFo::PdfStream::GetFilteredCopy(this=0x606000002f60, ppBuffer=0x7fffffffc6c0, lLen=0x7fffffffc6e0)
[#7] 0x7fafe1 → PoDoFo::PdfXRefStreamParserObject::ParseStream(this=0x7fffffffcaf0, nW=<optimized out>, rvecIndeces=<optimized out>)
[#8] 0x7f6fd3 → PoDoFo::PdfXRefStreamParserObject::ReadXRefTable(this=<optimized out>)
[#9] 0x7964b0 → PoDoFo::PdfParser::ReadXRefStreamContents(this=0x617000000080, lOffset=0x74, bReadOnlyTrailer=0x0)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
136		return calloc(nmemb, size);

```
