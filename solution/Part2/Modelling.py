import math
from solution.Part2.Counting import count


def moreEnglish(dataset, inString1, inString2, lambdas):
    countTable = {}
    score1 = score(dataset, inString1, countTable, lambdas)
    score2 = score(dataset, inString2, countTable, lambdas)
    print(score1)
    print(score2)
    return (score1 > score2)

def prob(dataset, inString, countTable, lambdas):
    ngrams = [inString[:i] for i in range(len(inString))]
    sum = 0.0
    for i in range(1, len(ngrams)):
        # lambdas[i-1]*
       if(count(dataset, ngrams[i-1], countTable) != 0): sum += count(dataset, ngrams[i], countTable)/count(dataset, ngrams[i-1], countTable)
    return sum

def score(dataset, inString, countTable, lambdas):
    words = [inString for inString in inString.split(' ')]
    sum = 0.0
    for i in range(0, len(words)):
        if(prob(dataset, words[i], countTable, lambdas) > 0.0): sum += math.log10(prob(dataset, words[i], countTable, lambdas))
    return sum

inString1 = "BLAH BL A BLAH"
inString2 = "THIS IS A TEST"
lambdas = [1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,0.888889]
dataset = open('../../ptb.train.txt', 'r').read()
print(moreEnglish(dataset, inString1, inString2, lambdas))