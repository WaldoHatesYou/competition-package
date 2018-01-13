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
    steps = int(steps)
    # convert to ascii
    ascii = [ord(c) for c in string]

    # add k steps modulo ascii range
    for i, c in enumerate(ascii):
        if c >= 65 or c <= 90:
            ascii[i] = (c + steps - 65) % 26 + 65

    # convert back to string
    return ''.join(chr(c) for c in ascii)

def decryptSimpleStep(string, steps):
    steps = int(steps)
    # convert to ascii
    ascii = [ord(c) for c in string]

    # add k steps modulo ascii range
    for i, c in enumerate(ascii):
        if c >= 65 or c <= 90:
            ascii[i] = (c - steps - 65) % 26 + 65

    # convert back to string
    return ''.join(chr(c) for c in ascii)

data_runner = DataRunner('input/1a.in')
data_runner.run('output/1a.out', encryptSimpleStep, decryptSimpleStep)