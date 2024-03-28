from cryptography.fernet import Fernet

print("Orgin:")
orgin = input()

print("Key:")
key = input()

decrypt = Fernet(orgin.encode()).decrypt(key.encode()).decode()

print("Key is:")
print(decrypt)
