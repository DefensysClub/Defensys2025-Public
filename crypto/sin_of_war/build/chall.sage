import random
from sage.all import *
import os

# Define parameters
q = 3329
Zq = Zmod(q)

def gen_key(n):
    first_row = random_vector(ZZ, n, -128, 128).change_ring(Zq)
    return matrix.circulant(first_row)

def enc_oracle(M, msg):
    if len(msg) != M.ncols():
        return f"You can only request encryption of messages of length {M.ncols()}"
    
    v = vector(bytes(msg))
    mask = random_vector(ZZ, M.nrows(), -q//2, q//2)
    enc = M.solve_right(v) + mask  
    return enc, mask

# Generate flag and matrix
with open("flag.txt", "r") as f:
    flag = f.read().strip().encode()

n = len(flag)
M = gen_key(n)
Minv = M^-1

def challenge():
    print("Welcome to the  Challenge!")
    print("You can only request one encryption of a chosen message.")
    
    # Encrypt the flag
    enc_flag, mask_flag = enc_oracle(Minv, flag)
    print(f"Encrypted flag: {enc_flag}")
    print(f"Mask of the encrypted flag: {mask_flag}")
    
    # Encrypt a chosen message
    hex_msg = input(f"Enter a hex-encoded message of length {2*n}: ").strip()
    try:
        msg = bytes.fromhex(hex_msg)
        if len(msg) != n:
            print(f"Message must be exactly {n} bytes long.")
        else:
            enc_msg, mask_msg = enc_oracle(Minv, msg)
            print(f"Encrypted message: {enc_msg}")
    except ValueError:
        print("Invalid hex input.")
    
    print("Exiting challenge.")

if __name__ == "__main__":
    challenge()