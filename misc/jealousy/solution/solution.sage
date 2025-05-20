from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# extract n and parts of p
n = 0x9583a49132368faff0d01e4c9f3525da704958b5329e4e54cb0d766166680b2d28fab9565f70874c98b9aa11c28be0ea815e165d59c73f8a0710772d3d793acd341f6e176eeb4f4fa059dd6a1d28e60ef008e7cf6d3bf03eb20e075b7e63e81860dcc4cc23d5d28288637537e5d2a543af81c1d9d171c603e0da044e19566d46c835dcb48f1b32cd3deb69f4daaa9dd065c01b8cdeef5c78e9fd6b3d60248eca1c24e68bfbfd28c0722139114f8e25b8540bc71b767bb0e3f7074d3e6cbafada7a9a8e97967b6fc233bd22117f8d54c2985bc4213847dbd5c9cf3c3d984969e685eca6c5e344fc45694c9d05e0b53280c76115b8095f309910c145ea76bae043

p_part = 0xbe470da7c7a7946540a996309dc0311bc928e6465683f91278475fc5d6f4730ea553318655f48195f8fe8f84ed67e28341b04ae0ee900d9917a5fb9366e8d800cfcb82c187fd2414e579957e978e32999d6c1c6d380f8cfc6a19909a8c9ea2000000000000000000000000000000000000000000000000000000000000000000

P.<x> = Zmod(n)[]
f = p_part + x 

sol = f.small_roots(beta=0.4, X=2**(68*4))[0]
p = int(p_part + sol)

q = int(n) // p 

e = 65537

d = int(pow(e, -1, (p-1)*(q-1)))

private_numbers = rsa.RSAPrivateNumbers(
    p=p,
    q=q,
    d=d,
    dmp1=int(d % (p - 1)),
    dmq1=int(d % (q - 1)),
    iqmp=int(pow(q, -1, p)),
    public_numbers=rsa.RSAPublicNumbers(e=int(e), n=int(n) )
)

private_key = private_numbers.private_key(backend=default_backend())
print(private_key)

with open("encrypted_flag.bin", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()


decrypted_message = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
print("Decrypted message:", decrypted_message.decode())

