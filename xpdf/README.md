## Description

 [xpdf](https://www.xpdfreader.com/)  is a free PDF viewer and toolkit, including a text extractor, image converter, HTML converter, and more. Most of the tools are available as open source.

## Version

[xpdf-4.00](https://www.xpdfreader.com/)

## Others

this bug is reported by fish@360TeamSeri0us, 
please send email to teamSeri0us360@gmail.com if you have some quetion.

## Details



```
1. pdftohtml 


./pdftohtml -f 1 xpdf-stack-overflow-poc-1 /dev/null

 AddressSanitizer: stack-overflow /src/xpdf-4.00/xpdf/XRef.cc:1021 XRef::fetch(int, int, Object*, int)
 


=================================================================
==1749==ERROR: AddressSanitizer: stack-overflow on address 0x7ffc99ea9f7c (pc 0x0000005afd85 bp 0x7ffc99eaa2a0 sp 0x7ffc99ea9f70 T0)
    #0 0x5afd84 in XRef::fetch(int, int, Object*, int) /src/xpdf-4.00/xpdf/XRef.cc:1021
    #1 0x566e2f in Object::fetch(XRef*, Object*, int) /src/xpdf-4.00/xpdf/Object.cc:115
    #2 0x48508f in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:244
    #3 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #4 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #5 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #6 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #7 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #8 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #9 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #10 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #11 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #12 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #13 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #14 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #15 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #16 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #17 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #18 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #19 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #20 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #21 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #22 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #23 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #24 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #25 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #26 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #27 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #28 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #29 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #30 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #31 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #32 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #33 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #34 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #35 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #36 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #37 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #38 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #39 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #40 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #41 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #42 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #43 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #44 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #45 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #46 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #47 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #48 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #49 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #50 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #51 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #52 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #53 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #54 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #55 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #56 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #57 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #58 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #59 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #60 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #61 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #62 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #63 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #64 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #65 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #66 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #67 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #68 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #69 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #70 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #71 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #72 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #73 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #74 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #75 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #76 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #77 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #78 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #79 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #80 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #81 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #82 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #83 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #84 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #85 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #86 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #87 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #88 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #89 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #90 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #91 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #92 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #93 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #94 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #95 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #96 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #97 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #98 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #99 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #100 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #101 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #102 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #103 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #104 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #105 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #106 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #107 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #108 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #109 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #110 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #111 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #112 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #113 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #114 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #115 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #116 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #117 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #118 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #119 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #120 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #121 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #122 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #123 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #124 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #125 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #126 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #127 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #128 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #129 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #130 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #131 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #132 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #133 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #134 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #135 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #136 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #137 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #138 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #139 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #140 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #141 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #142 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #143 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #144 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #145 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #146 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #147 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #148 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #149 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #150 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #151 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #152 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #153 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #154 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #155 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #156 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #157 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #158 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #159 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #160 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #161 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #162 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #163 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #164 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #165 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #166 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #167 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #168 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #169 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #170 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #171 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #172 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #173 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #174 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #175 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #176 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #177 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #178 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #179 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #180 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #181 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #182 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #183 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #184 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #185 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #186 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #187 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #188 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #189 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #190 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #191 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #192 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #193 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #194 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #195 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #196 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #197 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #198 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #199 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #200 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #201 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #202 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #203 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #204 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #205 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #206 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #207 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #208 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #209 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #210 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #211 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #212 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #213 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #214 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #215 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #216 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #217 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #218 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #219 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #220 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #221 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #222 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #223 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #224 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #225 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #226 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #227 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #228 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #229 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #230 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #231 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #232 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #233 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #234 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #235 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #236 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #237 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #238 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #239 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #240 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #241 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #242 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #243 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #244 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #245 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #246 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #247 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #248 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #249 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #250 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271
    #251 0x485260 in AcroForm::scanField(Object*) /src/xpdf-4.00/xpdf/AcroForm.cc:271

SUMMARY: AddressSanitizer: stack-overflow /src/xpdf-4.00/xpdf/XRef.cc:1021 XRef::fetch(int, int, Object*, int)
==1749==ABORTING

```



```
2. pdftoppm

./pdftoppm -f 1 xpdf-pdftoppm-heap-overflow-poc-1 /dev/null


 heap-buffer-overflow /src/xpdf-4.00/splash/SplashXPath.cc:245 SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode)


==1778==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6250000168f0 at pc 0x0000005fa775 bp 0x7fff0d31eee0 sp 0x7fff0d31eed0
READ of size 8 at 0x6250000168f0 thread T0
    #0 0x5fa774 in SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode) /src/xpdf-4.00/splash/SplashXPath.cc:245
    #1 0x5fc972 in SplashXPath::SplashXPath(SplashPath*, double*, double, int, int, SplashStrokeAdjustMode) /src/xpdf-4.00/splash/SplashXPath.cc:102
    #2 0x5d556a in Splash::fillWithPattern(SplashPath*, int, SplashPattern*, double) /src/xpdf-4.00/splash/Splash.cc:2935
    #3 0x5efed4 in Splash::strokeWide(SplashPath*, double, int, int) /src/xpdf-4.00/splash/Splash.cc:2611
    #4 0x5f0bcf in Splash::stroke(SplashPath*) /src/xpdf-4.00/splash/Splash.cc:2467
    #5 0x455744 in SplashOutputDev::stroke(GfxState*) /src/xpdf-4.00/xpdf/SplashOutputDev.cc:1640
    #6 0x4b9a28 in Gfx::opStroke(Object*, int) /src/xpdf-4.00/xpdf/Gfx.cc:1652
    #7 0x49f319 in Gfx::execOp(Object*, Object*, int) /src/xpdf-4.00/xpdf/Gfx.cc:826
    #8 0x49f6d9 in Gfx::go(int) /src/xpdf-4.00/xpdf/Gfx.cc:719
    #9 0x49fec5 in Gfx::display(Object*, int) /src/xpdf-4.00/xpdf/Gfx.cc:641
    #10 0x54ad28 in Page::displaySlice(OutputDev*, double, double, int, int, int, int, int, int, int, int, int (*)(void*), void*) /src/xpdf-4.00/xpdf/Page.cc:373
    #11 0x54b1bc in Page::display(OutputDev*, double, double, int, int, int, int, int (*)(void*), void*) /src/xpdf-4.00/xpdf/Page.cc:323
    #12 0x54f469 in PDFDoc::displayPage(OutputDev*, int, double, double, int, int, int, int, int (*)(void*), void*) /src/xpdf-4.00/xpdf/PDFDoc.cc:388
    #13 0x45d475 in main /src/xpdf-4.00/xpdf/pdftoppm.cc:229
    #14 0x7fee9507a82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #15 0x440f88 in _start (/src/xpdf-4.00/build/test/bin/pdftoppm+0x440f88)

0x6250000168f0 is located 16 bytes to the left of 8768-byte region [0x625000016900,0x625000018b40)
allocated by thread T0 here:
    #0 0x7fee96224602 in malloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98602)
    #1 0x59b978 in gmalloc /src/xpdf-4.00/goo/gmem.cc:140

SUMMARY: AddressSanitizer: heap-buffer-overflow /src/xpdf-4.00/splash/SplashXPath.cc:245 SplashXPath::strokeAdjust(SplashXPathPoint*, SplashPathHint*, int, SplashStrokeAdjustMode)
Shadow bytes around the buggy address:
  0x0c4a7fffacc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4a7fffacd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4a7ffface0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4a7fffacf0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c4a7fffad00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c4a7fffad10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]fa
  0x0c4a7fffad20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4a7fffad30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4a7fffad40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4a7fffad50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c4a7fffad60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==1778==ABORTING



```



```
3. pdfinfo

./pdfinfo -f 1 xpdf-stack-overflow-poc-1 /dev/null


=================================================================
==1914==ERROR: AddressSanitizer: stack-overflow on address 0x7ffeaa429ff8 (pc 0x000000566ae1 bp 0x7ffeaa42a030 sp 0x7ffeaa42a000 T0)
    #0 0x566ae0 in XRef::fetch(int, int, Object*, int) /src/xpdf-4.00/xpdf/XRef.cc:1035
    #1 0x51da5b in Object::fetch(XRef*, Object*, int) /src/xpdf-4.00/xpdf/Object.cc:115
    #2 0x451280 in Array::get(int, Object*) /src/xpdf-4.00/xpdf/Array.cc:62
    #3 0x4531f0 in Object::arrayGet(int, Object*) /src/xpdf-4.00/xpdf/Object.h:243
    #4 0x4531f0 in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:495
    #5 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #6 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #7 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #8 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #9 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #10 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #11 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #12 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #13 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #14 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #15 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #16 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #17 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #18 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #19 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #20 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #21 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #22 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #23 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #24 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #25 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #26 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #27 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #28 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #29 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #30 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #31 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #32 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #33 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #34 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #35 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #36 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #37 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #38 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #39 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #40 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #41 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #42 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #43 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #44 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #45 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #46 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #47 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #48 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #49 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #50 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #51 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #52 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #53 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #54 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #55 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #56 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #57 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #58 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #59 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #60 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #61 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #62 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #63 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #64 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #65 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #66 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #67 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #68 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #69 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #70 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #71 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #72 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #73 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #74 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #75 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #76 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #77 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #78 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #79 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #80 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #81 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #82 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #83 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #84 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #85 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #86 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #87 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #88 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #89 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #90 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #91 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #92 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #93 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #94 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #95 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #96 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #97 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #98 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #99 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #100 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #101 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #102 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #103 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #104 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #105 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #106 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #107 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #108 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #109 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #110 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #111 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #112 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #113 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #114 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #115 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #116 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #117 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #118 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #119 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #120 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #121 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #122 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #123 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #124 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #125 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #126 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #127 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #128 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #129 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #130 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #131 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #132 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #133 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #134 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #135 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #136 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #137 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #138 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #139 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #140 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #141 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #142 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #143 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #144 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #145 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #146 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #147 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #148 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #149 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #150 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #151 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #152 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #153 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #154 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #155 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #156 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #157 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #158 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #159 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #160 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #161 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #162 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #163 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #164 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #165 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #166 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #167 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #168 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #169 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #170 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #171 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #172 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #173 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #174 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #175 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #176 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #177 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #178 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #179 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #180 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #181 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #182 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #183 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #184 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #185 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #186 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #187 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #188 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #189 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #190 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #191 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #192 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #193 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #194 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #195 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #196 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #197 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #198 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #199 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #200 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #201 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #202 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #203 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #204 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #205 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #206 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #207 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #208 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #209 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #210 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #211 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #212 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #213 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #214 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #215 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #216 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #217 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #218 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #219 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #220 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #221 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #222 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #223 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #224 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #225 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #226 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #227 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #228 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #229 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #230 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #231 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #232 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #233 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #234 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #235 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #236 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #237 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #238 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #239 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #240 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #241 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #242 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #243 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #244 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #245 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #246 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #247 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #248 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #249 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #250 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #251 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #252 0x4531fd in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496

SUMMARY: AddressSanitizer: stack-overflow /src/xpdf-4.00/xpdf/XRef.cc:1035 XRef::fetch(int, int, Object*, int)
==1914==ABORTING


```





```

4. pdffonts

./pdffonts -f 1 xpdf-stack-overflow-poc-1 /dev/null


ASAN:SIGSEGV
=================================================================
==346==ERROR: AddressSanitizer: stack-overflow on address 0x7ffc58b2bf3c (pc 0x000000566d31 bp 0x7ffc58b2c100 sp 0x7ffc58b2bf30 T0)
    #0 0x566d30 in XRef::fetch(int, int, Object*, int) /src/xpdf-4.00/xpdf/XRef.cc:1021
    #1 0x51dddb in Object::fetch(XRef*, Object*, int) /src/xpdf-4.00/xpdf/Object.cc:115
    #2 0x451600 in Array::get(int, Object*) /src/xpdf-4.00/xpdf/Array.cc:62
    #3 0x453570 in Object::arrayGet(int, Object*) /src/xpdf-4.00/xpdf/Object.h:243
    #4 0x453570 in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:495
    #5 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #6 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #7 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #8 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #9 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #10 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #11 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #12 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #13 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #14 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #15 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #16 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #17 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #18 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #19 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #20 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #21 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #22 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #23 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #24 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #25 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #26 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #27 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #28 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #29 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #30 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #31 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #32 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #33 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #34 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #35 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #36 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #37 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #38 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #39 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #40 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #41 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #42 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #43 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #44 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #45 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #46 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #47 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #48 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #49 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #50 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #51 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #52 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #53 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #54 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #55 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #56 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #57 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #58 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #59 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #60 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #61 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #62 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #63 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #64 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #65 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #66 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #67 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #68 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #69 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #70 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #71 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #72 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #73 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #74 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #75 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #76 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #77 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #78 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #79 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #80 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #81 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #82 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #83 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #84 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #85 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #86 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #87 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #88 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #89 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #90 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #91 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #92 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #93 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #94 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #95 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #96 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #97 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #98 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #99 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #100 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #101 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #102 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #103 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #104 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #105 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #106 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #107 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #108 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #109 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #110 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #111 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #112 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #113 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #114 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #115 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #116 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #117 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #118 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #119 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #120 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #121 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #122 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #123 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #124 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #125 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #126 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #127 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #128 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #129 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #130 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #131 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #132 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #133 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #134 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #135 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #136 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #137 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #138 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #139 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #140 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #141 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #142 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #143 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #144 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #145 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #146 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #147 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #148 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #149 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #150 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #151 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #152 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #153 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #154 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #155 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #156 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #157 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #158 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #159 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #160 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #161 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #162 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #163 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #164 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #165 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #166 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #167 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #168 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #169 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #170 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #171 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #172 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #173 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #174 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #175 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #176 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #177 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #178 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #179 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #180 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #181 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #182 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #183 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #184 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #185 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #186 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #187 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #188 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #189 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #190 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #191 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #192 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #193 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #194 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #195 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #196 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #197 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #198 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #199 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #200 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #201 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #202 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #203 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #204 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #205 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #206 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #207 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #208 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #209 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #210 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #211 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #212 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #213 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #214 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #215 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #216 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #217 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #218 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #219 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #220 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #221 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #222 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #223 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #224 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #225 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #226 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #227 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #228 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #229 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #230 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #231 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #232 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #233 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #234 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #235 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #236 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #237 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #238 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #239 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #240 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #241 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #242 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #243 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #244 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #245 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #246 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #247 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #248 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #249 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #250 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #251 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
    #252 0x45357d in Catalog::countPageTree(Object*) /src/xpdf-4.00/xpdf/Catalog.cc:496
SUMMARY: AddressSanitizer: stack-overflow /src/xpdf-4.00/xpdf/XRef.cc:1021 XRef::fetch(int, int, Object*, int)


```
