input = "ALPHABETIZE! THIS!"
keys = [1,3,5]
output = ""
j = 0
for i in range(0,len(input)):
    if(ord(input[i]) >= 65 and ord(input[i]) <= 90):
        output += chr((((ord(input[i])+keys[j]) - 65) % 26) + 65)
        j = (j + 1) % (len(keys))
    else: output += input[i]
print(input)
print(output)