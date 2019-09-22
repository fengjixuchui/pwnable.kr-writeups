#http://pwnable.kr/
#pwnable.kr flag solution
#pwn4magic

import os
import os.path
import time
import sys
from subprocess import call

PATH='flag'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "[+]File Exists! ^_^"
    print
    time.sleep(2)
    print "[+]Step 1 : We run strings & we find out UPX!"
    call('strings flag | grep "UPX!"', shell=True)
    time.sleep(2)
    print "[+]Step 2 : We install UPX"
    call('apt-get install upx-ucl', shell=True)
    time.sleep(2)
    print "[+]Step 3 : We decompress the flag binary"
    call('upx-ucl -q -d flag', shell=True)
    time.sleep(2)
    print "[+]Step 4 : We grab the flag \O/"
    call('strings flag | grep "UPX"', shell=True)
else:
    print "File Is Missing :("
    time.sleep(1)
    sys.exit("Bye..")
