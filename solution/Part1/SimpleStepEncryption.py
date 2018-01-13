# Input: ENCRYPT|3|ALPHABETIZE!
#
#     ALPHABETIZE!        <- shift one position in the alphabet for each step
# k=1 BMQIBCFUJAF!        <- note: Z shifts to A
# k=2 CNRJCDGVKBG!
# k=3 DOSKDEHWLCH!
#
# Output: DOSKDEHWLCH!

def step(steps, string):
    # convert to ascii
    ascii = [ord(c) for c in string]

    # add k steps modulo ascii range
    for i, c in enumerate(ascii):
        if c >= 65 or c <= 90:
            ascii[i] = (c + steps - 65) % 26 + 65

    # convert back to string
    return ''.join(chr(c) for c in ascii)


for i in range(1,4):
    print(step(i, "ALPHABETIZE!"))

