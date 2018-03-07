def loadsonnets(dictname = 'data/Syllable_dictionary.txt', filename='data/shakespeare.txt'):
    endofline = -1
#    word2index = {}
#    word2nsyll = []
#    index = 0
#    #dictre = re.compile(r'([A-Za-z\'\-]+)\s(E[0-9]+)')
#    with DICT as open(dictname):
#        for line in DICT:
#            tokens = line.strip().split()
#
#            if 


    # read in syllable dictionary
    f = open("data/Syllable_dictionary.txt","r")
    counter = 0
    word2syll={}
    word2num={}
    num2word={}
    for line in f:
        Dict_item = line.strip().split(' ')
        #word2syll[Dict_item[0]] = Dict_iterm[1:]
        word2syll.update({Dict_item[0]:Dict_item[1:]})
        word2num.update({Dict_item[0]:counter})
        num2word.update({counter:Dict_item[0]})
        counter = counter + 1

    sonnets = []
    with FILE = open(filename):
        insidesonnet = False
        for line in FILE:
            tokens = line.strip().split()
            if not(len(tokens) > 1):
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
