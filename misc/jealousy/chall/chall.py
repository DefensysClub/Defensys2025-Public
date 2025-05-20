from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

print(private_key.private_numbers().p, private_key.private_numbers().q)

# Export private key to PEM file
with open("private_key_1.pem", "wb") as private_key_file:
    private_key_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()  # Use password-based encryption if needed
        )
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

print("RSA key pair generated and saved to 'private_key.pem' and 'public_key.pem'")
