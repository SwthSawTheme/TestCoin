from models.usuarios import *
from models.transacoes import *

if __name__ == "__main__":

    user1 = Usuario()
    user2 = Usuario()
    user3 = Usuario()

    # Dados da transação 1
    dados_transacao1 = {"remetente": "user1", "destinatario": "user2", "valor": 100}
    
    # Transação 1
    transacao1 = Transacao(user1.public_key,user1.private_key, dados_transacao1)
    print("Transação 1 válida?", transacao1.verificar_assinatura(user1.public_key))

    # Dados da transação 2
    dados_transacao2 = {"remetente": "user2", "destinatario": "user3", "valor": 50}
    transacao2 = Transacao(user2.public_key,user2.private_key, dados_transacao2)
    print("Transação 2 válida?", transacao2.verificar_assinatura(user2.public_key))
