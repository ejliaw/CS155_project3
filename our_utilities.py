def loadsonnets(dictname = 'data/Syllable_dictionary.txt', filename='data/shakespeare.txt'):
    """
    input: filenames, which you can give according to where the files are in your laptop.
    output:
        sonnets: a Python list of lists. sonnets[0] is the 1st Sonnet and is a list of integers that represent all the words in the sonnet. End of line is encoded as '-1'.
        word2syll: a Python dictionary that maps the word to a list of strings e.g. ["E2", "3"]
        word2index: a Python dictionary that maps the word to its integer index (0 based).
        index2word: a Python dictionary that maps integer indices back to words.
    """
# end of line is a special emission that denotes the end of a line of poetry. It will follow the last word of each line, including after the last word of the last line of a poem.
    endofline = -1
# punctuation is a string of all the punctionation marks present in shakespeare.txt
    left_punctuation = ":.,?!;()" #Don't remove the initial apostrophe!
    right_punctuation = ":.,'?!;()"

# Parse the Syllable_dictionary file.
    counter = 0
    word2index = {}
    word2syll = {}
    with open(dictname) as DICT:
        for line in DICT:
            tokens = line.strip().split()
            word = tokens[0].lstrip(leftpunctuation).rstrip(rightpunctuation).lower()
            word2index[word] = counter
            counter = counter + 1
            word2syll[word] = tokens[1:]

    word2index["\\"] = endofline
    index2word = {word2index[key]:key for key in word2index}

# Read in each sonnet.
    sonnets = []
    sonnet = [] # Necessary to avoid an UnboundLocalError?
    with open(filename) as FILE:
        insidesonnet = False
        for line in FILE:
            tokens = line.strip().split()
            if not (len(tokens) > 1):
                if insidesonnet:
                    sonnets.append(sonnet)
                    sonnet = []
                    insidesonnet = False
                else:
                    pass
            else:
                if not insidesonnet:
                    insidesonnet = True
                for word in tokens:
                    word = word.lstrip(leftpunctuation).rstrip(rightpunctuation).lower()
                    if word in word2index:
                        w = word2index[word]
                        sonnet.append(w)
                    else:
                        print("Word {} not in index".format(word))
                sonnet.append(endofline)

    return sonnets, word2syll, word2index, index2word
