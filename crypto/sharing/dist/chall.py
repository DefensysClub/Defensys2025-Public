import ecdsa
import hashlib
import os
from Crypto.Util.number import *


Flag = "defensys{redacted}"

p = getPrime(256)

private_key = os.urandom(31)
poly = [os.urandom(31) for _ in range(10)] + [private_key]
poly = list(map(bytes_to_long, poly) )

curve = ecdsa.SECP256k1
generator = curve.generator
order = curve.order

def shamir_split(poly):
    num_shares = len(poly)
    def eval_poly(poly, x):
        ans = 0
        for i, coeff in enumerate(poly[::-1]):
            ans += x**i * coeff
            ans %= p
        return ans

    shares = []
    for i in range(1, num_shares + 1):
        x = i
        y = eval_poly(poly, x)
        shares.append((x, y))
    return shares

def lagrange_interpolation(x, points, p):
    result = 0
    n = len(points)
    
    for i in range(n):
        
        xi, yi = points[i]
        li = 1 

        for j in range(n):
            if i != j:
                xj, _ = points[j]
                numerator = (x - xj) % p
                denominator = (xi - xj) % p
                li *= (numerator * pow(denominator, -1, p)) % p
                li %= p
        result += (yi * li) % p
        result %= p

    return result

shares = shamir_split(poly)

print("Hello World")
print("Here is your part of the secret key please enter it so we can generate our public key")
print(shares[0])

# sending each user his own share
# ...

counter = 0

while counter <= 300:
    print("[1] calculate public key")
    print("[2] verify secret key")
    print("[3] exit")
    choice = input("choose an options ")

    if choice == "1":
        
        try:
            your_share = tuple(map(int,input("Enter your share: ").strip("").split(",")))
            if len(your_share) != 2:
                print("Invalid share")
                continue
            
        except:
            print("Invalid input")

        # Asking other users to enter their shares too
        # ...

        all_shares = [your_share] + shares[1:]

        recovered_secret = lagrange_interpolation(0, all_shares, p)

        private_key = recovered_secret % order
        public_key = private_key * generator

        print("Public Key:", int(public_key.x()), int(public_key.y()) )
        counter += 1

    elif choice == "2":
        try:
            your_secret = int(input("Enter your secret key: "))
            if your_secret == private_key:
                print("Congrats! Here is the flag: ", Flag)
                break
            else:
                print("Invalid secret key")
                break
        except:
            print("Invalid input")
            break
    elif choice == "3":
        break

    else:
        print("invalid option")
        break

