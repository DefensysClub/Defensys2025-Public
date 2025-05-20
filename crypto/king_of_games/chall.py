from Crypto.Util.number import  getPrime as araPrime
from sympy import nextprime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256

flag = b"defensys{its_all_about_LJIDR_moraba3_and_some_coppersmith_oupss_no_need_for_it_here}" 

p = araPrime(1024)
q = nextprime( (p>>512)<<512 )
n = p * q

key = sha256(str(p+q).encode()).digest()[:16]
iv  = sha256(str(p-q).encode()).digest()[:16]

cipher = AES.new(key=key,iv=iv,mode=AES.MODE_CBC)
ct = cipher.encrypt(pad(flag,16))


print(f"n  = ",n)
print(f"iv = ",iv.hex())
print(f"ct = ",ct.hex())