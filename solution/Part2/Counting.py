
# count expects a preprocessed dataset, a match string, and a dictionary that has
# previously counted strings. If this is the first count just pass an empty dictionary

def count(dataset, ngram, dictionary):
    # if nothing is in the dictionary it means its the first time count has been used
    # a.k.a please preprocess dataset and change the pointer to the new dataset
    if not dictionary:
        dataset = preprocess(dataset)

    # otherwise check if the ngram is already in the existing map
    if ngram in dictionary:
        return dictionary[ngram]

    # otherwise add it to the dict
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
