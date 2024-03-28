import os
from cryptography.fernet import Fernet

decrypt = False

files = []

decrypt_key = input("Please input the key provided!\n")
binary = decrypt_key.encode()

with open("check.na12", "rb") as check:
    if Fernet(binary).decrypt(check.read()).decode() == "corr":
        print("Key correct, Decrypting Proceeded!")
        decrypt = True
    else:
        print("Wrong key! Bye!")


if decrypt:
    for file in os.listdir():
        if file == "encrypter.py" or file == "decrypter.py" or file == "encrypter.exe" or file == "decrypter.exe" or file == "encrypter" or file == "decrypter" or file == "key.na12" or file == "check.na12" or file == "orgin.na12" or file == "getkey.py" or file == "makekey.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    
    print("File detected:", files)

    for file in files:
        print("Getting data of:", file)
        with open(file, "rb") as thefile:
            contents = thefile.read()
        print("Decrypting data of:", file)
        contents_derypted = Fernet(binary).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_derypted)
        print("File", file, "has been decrypted!")
    
    print("All files decrypted!")
