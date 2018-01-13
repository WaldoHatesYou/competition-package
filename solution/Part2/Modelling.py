import math
from solution.Part2.Counting import count


def moreEnglish(inString1, inString2, lambdas):
    countTable = {}
    dataset = open('../../ptb.train.txt', 'r')
    score1 = score(dataset, inString1, countTable, lambdas)
    score2 = score(dataset, inString2, countTable, lambdas)

def prob(dataset, inString, countTable, lambdas):
    ngrams = [inString[:i] for i in range(len(inString))]
    sum = 0
    for i in range(1, len(ngrams)):
        sum += lambdas[i-1]*count(dataset, ngrams[i], countTable)/count(dataset, ngrams[i-1], countTable)
    return sum

def score(dataset, inString, countTable, lambdas):
    words = [inString for inString in inString.split(' ')]
    sum = 0
    for i in range(0, len(words)):
        sum += math.log10(prob(dataset, words[i], countTable, lambdas))
    return sum