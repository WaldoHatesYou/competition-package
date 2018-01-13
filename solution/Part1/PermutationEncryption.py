in_file = open("input/1c.in", "r")
in_lines = in_file.readlines()
in_file.close()

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

parameters = []
for line in in_lines:
    parameter_list = line.split(' | ')
    parameters.append((parameter_list[0], parameter_list[1], parameter_list[2]))

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

outputs = []

for parameter in parameters:
    TYPE,key,text = parameter
    if TYPE == ENCRYPT:
        outputs.append(encrypt(text, key))
    else:
        outputs.append(decrypt(text, key))

with open('output/1c.out', 'w') as out_file:
    for output in outputs:
        out_file.write("%s" % output)

