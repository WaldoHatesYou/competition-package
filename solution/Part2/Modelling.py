
def moreEnglish(string1, string2):
    return 0

def count():
    training = open('words.txt', 'r')
    print(training)
    return 0

def avg():
    return 0

def prob(string, count_table, lambdas):
    #TODO check that it also puts the whole string in ngrams
    #PLEASE DO IT JOEY
    ngrams = [string[:i] for i in range(len(string))]
