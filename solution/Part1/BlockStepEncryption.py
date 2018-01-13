from DataRunner import DataRunner

def encrypt(plaintext, key):
    keys = [int(key) for key in key.split(' ')]
    ciphertext = ""
    j = 0
    for i in range(0, len(plaintext)):
        if (ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90):
            ciphertext += chr((((ord(plaintext[i]) + keys[j]) - 65) % 26) + 65)
            j = (j + 1) % (len(keys))
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, key):
    keys = [int(key) for key in key.split(' ')]
    plaintext = ""
    j = 0
    for i in range(0, len(ciphertext)):
        if (ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90):
            plaintext += chr((((ord(ciphertext[i]) - keys[j]) - 65) % 26) + 65)
            j = (j + 1) % (len(keys))
        else:
            plaintext += ciphertext[i]
    return plaintext

data_runner = DataRunner('input/1b.in')
data_runner.run('output/1b.out', encrypt, decrypt)
