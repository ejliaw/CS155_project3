import time
from HMM import *

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
    endofline = 0 #-1
# punctuation is a string of all the punctionation marks present in shakespeare.txt
    #left_punctuation = ":.,?!;()" #Don't remove the initial apostrophe!
    #right_punctuation = ":.,'?!;()"
    punctuation = ":.,'?!;()"

# Parse the Syllable_dictionary file.
    counter = 0
    word2index = {}
    word2syll = {}

    word2index["\\"] = endofline
    counter += 1

    with open(dictname) as DICT:
        for line in DICT:
            tokens = line.strip().split()
            word = tokens[0].strip(punctuation).lower() #.lstrip(left_punctuation).rstrip(right_punctuation).lower()
            word2index[word] = counter
            counter = counter + 1
            word2syll[word] = tokens[1:]

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
                    word = word.strip(punctuation).lower() #.lstrip(left_punctuation).rstrip(right_punctuation).lower()
                    if word in word2index:
                        w = word2index[word]
                        sonnet.append(w)
                    else:
                        print("Word {} not in index".format(word))
                sonnet.append(endofline)

    return sonnets, word2syll, word2index, index2word

def writeHMM(myHMM, filename=None):
    '''takes a trained HMM object and saves its parameters to file.
    '''
    nHidden = myHMM.L
    nOmissions = myHMM.D
    nEpochs = myHMM.n_epochs

    if filename == None:
        uid = time.strftime('%d%H%M%S')
        filename = "HMM_{0:d}_{1:d}_{2}.txt".format(nHidden, nEpochs, uid)

    with open(filename, 'w') as FILE: 

        header = "{0}\t{1}\n".format(nHidden, nOmissions)
        FILE.write(header)

        A_start_row = "\t".join(["{:1.10e}".format(a_start) for a_start in myHMM.A_start]) + '\n'
        FILE.write(A_start_row)
        
        for row in myHMM.A:
            A_row = "\t".join(["{:1.10e}".format(a_ij) for a_ij in row]) + '\n'
            FILE.write(A_row)

        for row in myHMM.O:
            O_row = "\t".join(["{:1.10e}".format(o_ij) for o_ij in row]) + '\n'
            FILE.write(O_row)

def readHMM(filename):
    '''reads in our own tab-separated file format for HMMs. returns the corresponding HMM object.
    '''
    with open(filename, 'r') as FILE: 

        header = FILE.readline()
        L, D = [int(x) for x in header.strip().split()]

        A_start_row = FILE.readline()
        A_start = [float(x) for x in A_start_row.strip().split()]
        
        A = []
        for i in range(L):
            A_row = FILE.readline()
            A.append([float(x) for x in A_row.strip().split()])

        O = []
        for i in range(L):
            O_row = FILE.readline()
            O.append([float(x) for x in O_row.strip().split()])
    
    myHMM = HiddenMarkovModel(A, O)
    myHMM.A_start = A_start
    if L != myHMM.L: print("error in L")
    if D != myHMM.D: print("error in D")
    return myHMM
