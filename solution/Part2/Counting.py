### NOT FINISHED

def counting(dataset, ngram):
    # preprocess first
    string = preprocess(dataset)

    # dataset is preprocessed here


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
    # otherwise add



