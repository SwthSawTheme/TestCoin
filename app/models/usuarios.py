from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key,load_pem_parameters, Encoding, PrivateFormat, PublicFormat, NoEncryption


class Usuario:
    
    def __init__(self):
        # Gerar um par de chaves
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def export_private_key(self):
        return self.private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())
    
    def export_public_key(self):
        return self.public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)

    