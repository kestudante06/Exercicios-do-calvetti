from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Gera chave privada
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Mensagem
mensagem = b"Mensagem assinada"

# Assinatura
assinatura = private_key.sign(mensagem, ec.ECDSA(hashes.SHA256()))
print("Assinatura:", assinatura)

# Verificação
public_key.verify(assinatura, mensagem, ec.ECDSA(hashes.SHA256()))
print("Assinatura válida!")
