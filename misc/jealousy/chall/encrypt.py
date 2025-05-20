from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Load private key from PEM file
with open("private_key_1.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Generate corresponding public key
public_key = private_key.public_key()

# Export public key to PEM file
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
"""
# Extract and print p and q
if isinstance(private_key, rsa.RSAPrivateKey):
    numbers = private_key.private_numbers()
    p = numbers.p
    q = numbers.q
    print(f"p: {hex(p)[2:]}")
    print(f"q: {hex(q)[2:]}")
else:
    print("Loaded key is not an RSA private key")
"""

message = b"defensys{mablanx_a_eve_makhdma_ma_walo_hh_324123141234}"
with open("public_key.pem", "rb") as key_file:
    loaded_public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

ciphertext = loaded_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save ciphertext to a file
with open("encrypted_flag.bin", "wb") as encrypted_file:
    encrypted_file.write(ciphertext)
