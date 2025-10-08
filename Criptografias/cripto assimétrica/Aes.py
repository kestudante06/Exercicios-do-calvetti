#fazendo as importações necessárias
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

#Gerando chave aleatória de 16 bytes
key = get_random_bytes(16)

#Criando cifra AES no modo EAX
cipher = AES.new(key, AES.MODE_EAX)

#Mensagem
mensagem = b"Mensaagem ultra secreta com AES-eax"

#criptografia
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(mensagem)

print("CipherText:", ciphertext)
print("Tag:", tag)

#Descriptografia
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)

print("Mensagem decifrada:", plaintext.decode())