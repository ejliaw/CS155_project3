def loadsonnets(dictname = 'data/Syllable_dictionary.txt', filename='data/shakespeare.txt'):
    """
    input: filenames, which you can give according to where the files are in your laptop.
    output:
        sonnets: a Python list of lists. sonnets[0] is the 1st Sonnet and is a list of integers that represent all the words in the sonnet. End of line is encoded as '-1'.
        word2syll: a Python dictionary that maps the word to a list of strings e.g. ["E2", "3"]
        word2index: a Python dictionary that maps the word to its integer index (0 based).
        index2word: a Python dictionary that maps integer indices back to words.
    """
    endofline = -1

# read in syllable dictionary
    f = open(dictname, 'r')
    counter = 0
    word2syll = {}
    word2index = {}
    index2word = {}
    for line in f:
        Dict_item = line.strip().split(' ')
        word = Dict_item[0].lower().strip(':,?!.;\'')
        word2syll[word] = Dict_item[1:]
        word2index[word] = counter
        index2word[counter] = word
        counter = counter + 1

    sonnets = []
    sonnet = []
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
                    if word in word2index:
                        w = word2index[word]
                        sonnet.append(w)
                    else:
                        print("Word {} not in index".format(word))
                sonnet.append(endofline)

    return sonnets, word2syll, word2index, index2word
#    word2index = {}
#    word2nsyll = []
#    index = 0
#    #dictre = re.compile(r'([A-Za-z\'\-]+)\s(E[0-9]+)')
#    with DICT as open(dictname):
#        for line in DICT:
#            tokens = line.strip().split()
#
#            if 
        #word2syll[Dict_item[0]] = Dict_iterm[1:]

