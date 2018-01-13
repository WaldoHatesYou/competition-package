from DataRunner import DataRunner

# Input: ENCRYPT|3|ALPHABETIZE!
#
#     ALPHABETIZE!        <- shift one position in the alphabet for each step
# k=1 BMQIBCFUJAF!        <- note: Z shifts to A
# k=2 CNRJCDGVKBG!
# k=3 DOSKDEHWLCH!
#
# Output: DOSKDEHWLCH!


def encryptSimpleStep(string, steps):
    res = ''

    # add k steps modulo ascii range
    for i, c in enumerate(string):
        # convert to ascii
        x = ord(c)
        if 65 <= x <= 90:
            res += chr((x + int(steps) - 65) % 26 + 65)
        else:
            res += c

    # convert back to string
    return res


def decryptSimpleStep(string, steps):
    res = ''

    # add k steps modulo ascii range
    for i, c in enumerate(string):
        # convert to ascii
        x = ord(c)
        if 65 <= x <= 90:
            res += chr((x - int(steps) - 65) % 26 + 65)
        else:
            res += c
    # convert back to string
    return res

# print(encryptSimpleStep("REMEMBER TO WRAP PROPERLY", 25))
# print(encryptSimpleStep("THE KEY FOR THIS MESSAGE IS 5 (FIVE)", 5))
# print(encryptSimpleStep("THIS MESSAGE IS NOT ENCRYPTED", 0))
# print(encryptSimpleStep("ALPHABETIZE!", 3))
# print(decryptSimpleStep("ALPHABETIZE!", 3))
# print(decryptSimpleStep("DOSKDEHWLCH!", 3))

data_runner = DataRunner('input/1a.in')
data_runner.run('output/1a.out', encryptSimpleStep, decryptSimpleStep)