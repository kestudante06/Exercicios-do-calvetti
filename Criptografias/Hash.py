#importando o hashlib
import hashlib

#Digitando a mensagem
mensagem = input("Digite a mensagem que deseja criptografar: ")

#Criptografando a mensagem com SHA-256
hash_sha256 = hashlib.sha256(mensagem.encode()).hexdigest()

#Exibindo mensagem
print("SHA-256:", hash_sha256)