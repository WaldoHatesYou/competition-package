from DataRunner import DataRunner

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key):
    ciphertext = ""
    for character in plaintext:
        alphabet_index = ALPHABET.find(character)
        if alphabet_index != -1:
            ciphertext += key[alphabet_index]
        else:
            ciphertext += character
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for character in ciphertext:
        key_index = key.find(character)
        if key_index != -1:
            plaintext += ALPHABET[key_index]
        else:
            plaintext += character
    return plaintext

if __name__ == "__main__":
    data_runner = DataRunner('input/1c.in')
    data_runner.run('output/1c.out',encrypt,decrypt)
