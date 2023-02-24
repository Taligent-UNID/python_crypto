import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import random, string


def utf8(s: bytes):
    return str(s, 'utf-8')

# Crea las claves pares en la carpeta seleccionada
def create_pair_keys(filename : str):
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

# Encripta la password y genera el archivo cifrado
def encrypt_password(public_key,password,filename_encrypt):
    with open(public_key, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    encrypted = base64.b64encode(public_key.encrypt(
        password,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    ))
    with open(f'{filename_encrypt}/file_encrypted.txt', 'wb') as f:
        f.write(encrypted)

# Des encripta el archivo cifrado y retornando la password
def decrypt_password(path_private_key,file_encrypted):

    with open(path_private_key, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    with open(f'{file_encrypted}','rb') as f:
        encrypted = f.read()

    decrypted = private_key.decrypt(
        base64.b64decode(encrypted),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    )

    return decrypted

# Genera una password random alphanumerica de 20 caracteres
def generate_password():
    length = 20
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars) for i in range(length))
