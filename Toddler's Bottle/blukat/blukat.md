# pwnable.kr blukat writeup by pwn4magic

Challenge Description :
```
Sometimes, pwnable is strange...
hint: if this challenge is hard, you are a skilled player.

ssh blukat@pwnable.kr -p2222 (pw: guest)
```

After we connect to the pwnable.kr server, we can see these files :

```bash
blukat@prowl:~$ ls -la
total 36
drwxr-x---   4 root blukat     4096 Aug 16  2018 .
drwxr-xr-x 114 root root       4096 May 19 15:59 ..
-r-xr-sr-x   1 root blukat_pwn 9144 Aug  8  2018 blukat
-rw-r--r--   1 root root        645 Aug  8  2018 blukat.c
dr-xr-xr-x   2 root root       4096 Aug 16  2018 .irssi
-rw-r-----   1 root blukat_pwn   33 Jan  6  2017 password
drwxr-xr-x   2 root root       4096 Aug 16  2018 .pwntools-cache
blukat@prowl:~$ 
```

Let's run the binary first to see how it works.

```bash
blukat@prowl:~$ ./blukat
guess the password!
1234
wrong guess!
blukat@prowl:~$ 
```

A password system, let's run ltrace to intercepts library calls.

```bash
blukat@prowl:~$ ltrace ./blukat
__libc_start_main(0x4007fa, 1, 0x7ffdc6c04b08, 0x4008c0 <unfinished ...>
fopen("/home/blukat/password", "r")                                                    = 0x1db9010
fgets("cat: password: Permission denied"..., 100, 0x1db9010)                           = 0x6010a0
puts("guess the password!"guess the password!
)                                                            = 20
fgets(1234
"1234\n", 128, 0x7f7ffbae38e0)                                                   = 0x7ffdc6c049b0
strcmp("cat: password: Permission denied"..., "1234\n")                                = 50
puts("wrong guess!"wrong guess!
)                                                                   = 13
exit(0 <no return ...>
+++ exited (status 0) +++
blukat@prowl:~$ 
```

It uses strcmp, let's see what strcmp is doing.

`strcmp, strncmp - compare two strings`

So here compares our input `1234` with `cat: password: Permission denied`

So `cat: password: Permission denied` is the password, weird huh ?

Let's test it out!

```bash
blukat@prowl:~$ ./blukat 
guess the password!
cat: password: Permission denied
congrats! here is your flag: Pl3as_DonT_Miss_youR_GrouP_Perm!!
blukat@prowl:~$ 
```

Flag : `Pl3as_DonT_Miss_youR_GrouP_Perm!!`

pwntools exploit :

```python
#!/usr/bin/env python
from pwn import *
context.log_level = 'DEBUG'

log.info('pwnable.kr - blukat exploit by pwn4magic')

shell = ssh('blukat', 'pwnable.kr', password='guest', port=2222)

sh = shell.run('./blukat')

sh.recvline() #guess the password!

sh.sendline('cat: password: Permission denied')

log.success(sh.recvline())
```

\ (•◡•) / yay! See ya!
