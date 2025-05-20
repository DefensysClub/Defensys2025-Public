from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util.number import *
import random


flag = "Defensys{REDACTED}"


key = get_random_bytes(16)

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def encrypt_aes(k, data):
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(data)
    return ct_bytes

def encrypt(msg):
    if len(msg) != 32:
        raise ValueError("msg length must be 32")
    
    m0 = msg[:16]
    m1 = msg[16:]

    r = get_random_bytes(16)
    print(encrypt_aes(key, r) , m0)
    return r + xor(encrypt_aes(key, r) , m0) + xor(encrypt_aes(key, m0), m1)


def main():
    print("hello this is a service to test the security of our encryption scheme")

    seen_before = []
    

    for round in range(128):
        message0 = bytes.fromhex(input("Enter the first message: "))
        message1 = bytes.fromhex(input("Enter the second message: "))

        if len(message0) != 32 or len(message1) != 32:
            print("Invalid message length")
            return

        if message0 in seen_before or message1 in seen_before:
            print("You have already entered this message")
            return

        seen_before.append(message0)
        seen_before.append(message1)

        b = random.randint(0, 1)

        output = encrypt(message0  if b == 0 else message1 )
        print(f"Here is the output: {output.hex()} {b}")

        ans = int(input("Enter 0 or 1 to guess which message was encrypted : "))

        if ans == b:
            print(f"{round} Nice Nice now continue working")
        else:
            print("Wrong guess")
            return
        
    print("Great Job here is your flag: ", flag)

if __name__ == "__main__":
    main()