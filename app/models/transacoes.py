from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import json

# Classe para representar uma transação
class Transacao:
    def __init__(self, public_key_sender, private_key_sender, data):
        self.public_key_sender = public_key_sender
        self.data = data  # Informações da transação (ex.: valor, destinatário)
        self.hash = self._create_hash(data)
        self.signature = self._sign(private_key_sender)
    
    def _create_hash(self, data):
        # Cria um hash dos dados
        digest = hashes.Hash(hashes.SHA256())
        digest.update(json.dumps(data).encode('utf-8'))
        return digest.finalize()
    
    def _sign(self, private_key):
        # Assina o hash dos dados com a chave privada
        return private_key.sign(
            self.hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    
    def verificar_assinatura(self, public_key):
        # Verifica a assinatura usando a chave pública
        try:
            public_key.verify(
                self.signature,
                self.hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False