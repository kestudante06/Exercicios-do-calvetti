from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Gera par de chaves
key = RSA.generate(2048)
public_key = key.publickey()
cipher = PKCS1_OAEP.new(public_key)

# Mensagem
mensagem = b"Segredo com RSA"

# Criptografando com chave pública
ciphertext = cipher.encrypt(mensagem)
print("Cifrado:", ciphertext)

# Decifrando com chave privada
cipher_dec = PKCS1_OAEP.new(key)
plaintext = cipher_dec.decrypt(ciphertext)
print("Decifrado:", plaintext.decode())
