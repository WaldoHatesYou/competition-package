### NOT FINISHED


def count(dataset, ngram, dictionary):
    if ngram in dictionary:
        return dictionary[ngram]

    dictionary[ngram] = dataset.count(ngram)

    return dictionary[ngram]

def preprocess(dataset):
    # define unwanted string literals
    # could use an arbitrary list but then would need to iterate through list
    # of undesirables

    unk = "<unk>"
    n = "N"

    # we will save non alphnumeric characters for after when checking words using regex

    # split the dataset by spaces into list
    wordList = dataset.split()

    # define resulting string
    res = ''

    # iterate through list
    # if undesirable skip
    for word in wordList:
        if word == unk or word == n:
            continue
        else:
            # otherwise add all alphanumeric
            for c in word:
                if c.isalpha():
                    res += c.upper()

    return res
