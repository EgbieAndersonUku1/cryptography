

def encrypt(plain_text):
    return plain_text[::-1]

def decrypt(cipher):
    return cipher[::-1]


message = "The way of the dragon"
cipher  = encrypt(message)
translated = decrypt(cipher)


print(cipher)
print(translated)


