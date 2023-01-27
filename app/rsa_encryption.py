import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import random, string


def utf8(s: bytes):
    return str(s, 'utf-8')

# Crea las claves pares en la carpeta "keys"
def create_pair_keys(filename):
    private_key = rsa.generate_private_key(
       public_exponent=65537,
       key_size=4096,
       backend=default_backend()
    )
    public_key = private_key.public_key()


    private_pem = private_key.private_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PrivateFormat.PKCS8,
       encryption_algorithm=serialization.NoEncryption()
    )

    with open(f'{filename}/private_key.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = public_key.public_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(f'{filename}/public_key.pem', 'wb') as f:
        f.write(public_pem)

def encrypt_password():
    with open("keys/public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    plaintext = b'agAyYzeEFzV.AhDx6qqzzYRbsb.7zvX8'
    encrypted = base64.b64encode(public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    ))
    with open('files/file_encrypted.txt', 'wb') as f:
        f.write(encrypted)

def decrypt_password(path_private_key):

    with open(f"{path_private_key}", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    with open('files/file_encrypted.txt','rb') as f:
        encrypted = f.read()

    decrypted = private_key.decrypt(
        base64.b64decode(encrypted),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    )

    with open('files/file_decrypted.txt','wb') as f:
        f.write(decrypted)


def generate_password():
    length = 20
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars) for i in range(length))