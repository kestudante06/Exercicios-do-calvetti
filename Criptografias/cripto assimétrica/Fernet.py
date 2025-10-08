from cryptography.fernet import Fernet

# Gera chave
key = Fernet.generate_key()
cipher = Fernet(key)

# Criptografa
mensagem = b"Mensagem secreta!"
token = cipher.encrypt(mensagem)
print("Cifrado:", token)

# Descriptografa
original = cipher.decrypt(token)
print("Decifrado:", original.decode())
