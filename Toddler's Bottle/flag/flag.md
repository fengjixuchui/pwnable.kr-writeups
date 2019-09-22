# pwnable.kr flag writeup by pwn4magic

Challenge Description :
```
Papa brought me a packed present! let's open it.

Download : http://pwnable.kr/bin/flag

This is reversing task. all you need is binary
```

Let's download the binary.

```bash
root@pwn4magic:~/Desktop/pwnable.kr# wget -q http://pwnable.kr/bin/flag
root@pwn4magic:~/Desktop/pwnable.kr# file flag
flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
root@pwn4magic:~/Desktop/pwnable.kr# 
```

So we have an 64bit ELF, let's run strings on it.

```bash
root@pwn4magic:~/Desktop/pwnable.kr# strings flag
...
...
UPX!
UPX!
```

We can see UPX! in the end. What UPX is ?

`UPX is a free, portable, extendable, high-performance executable packer for several executable formats.`

Let's search & install it.

```bash
oot@pwn4magic:~/Desktop/pwnable.kr# apt-cache search upx
clamav - anti-virus utility for Unix - command-line interface
upx-ucl - efficient live-compressor for executables
root@pwn4magic:~/Desktop/pwnable.kr# apt-get install upx-ucl
```

Now let's decompress the binary & grab the flag!

```bash
root@pwn4magic:~/Desktop/pwnable.kr# upx-ucl -d flag
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2018
UPX 3.95        Markus Oberhumer, Laszlo Molnar & John Reiser   Aug 26th 2018

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.
root@pwn4magic:~/Desktop/pwnable.kr# strings flag | grep UPX
UPX...? sounds like a delivery service :)
root@pwn4magic:~/Desktop/pwnable.kr# 
```

Flag : `UPX...? sounds like a delivery service :)`

\ (•◡•) / yay! See ya!
