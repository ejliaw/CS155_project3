from HMM import *
from our_utilities import *
import numpy as np
from collections import defaultdict

sonnets, word2syll, word2index, index2word = loadsonnets()

nwords = len(word2index.keys())
n = 3

# Okay, math is always correct. 3206**3 = 1e10 floats, which is several Gbs of RAM...
#jointprob = np.zeros( (nwords,)*(n) )
jointprob = defaultdict(list)

for sonnet in sonnets:
    length = len(sonnet)
    for i in range(length - n):
        prevs = tuple(sonnet[i:i+n-1])
        output = int(sonnet[i+n-1]) #sonnet[i+n-1:i+n] has an extra list around it.
        jointprob[prevs].append(output)

#normsum = np.sum(jointprob, axis=-1) #jointprob = jointprob / np.expand_dim(normsum, n-1)

seedsentence = "shall i" #compare"
seed = [word2index[word] for word in seedsentence.split()]
prevs = tuple(seed) #tuple(seed[:-1]) #curr = int(seed[-1])
how_sparse_debug = 0
newsonnet = [seed] #newsonnet = []
n_syllables = len(seed)
for i in range(14):
    line = []
    print("line: {}".format(i))
    attempts = 0
    while True: # A do while loop in python #P = jointprob[prevs]
        print(prevs, n_syllables)
        choices = jointprob[prevs]
        maxattempts = max(len(choices), 10)
        #if prevs in jointprob: # Doesn't work for defaultdicts!
        if len(choices) > 0:
            newword = int(np.random.choice(choices, 1))
        else:
            #newword = int(np.random.choice(nwords, 1))
            how_sparse_debug += 1
            print("aww... fell off the track with ", end="")
            print(prevs, [index2word[w] for w in prevs])
            while len(choices) <= 0:
                rline = int(np.random.choice(len(newsonnet), 1))
                rword = int(np.random.choice(len(newsonnet[rline])-1, 1))
                prevs = tuple(newsonnet[rline][rword:rword+1])
                choices = jointprob[prevs]
                maxattempts = max(len(choices), 10)
        line.append(newword)
        #newsonnet.append(newword)
        if newword == 0: # The end of line character.
            new_syllables = 0
        else:
            new_syllables = int(word2syll[index2word[newword]][0][-1])
        n_syllables += new_syllables
        if n_syllables > 10 and attempts < maxattempts:
            print("yo {} {}".format(attempts, maxattempts))
            del line[-1] # Erase the last step
            n_syllables -= new_syllables
            attempts += 1
        elif n_syllables == 10 or attempts >= maxattempts:
            prevs = prevs[1:] + (newword,)
            break 
        else:
            prevs = prevs[1:] + (newword,)
    newsonnet.append(line)
    n_syllables = 0

test = newsonnet
zerothline = test[0]
firstline = test[1]
zerothline.extend(firstline)
del test[1]
#testnewsonnet = [zerothline.extend(firstline)] + newsonnet[2:]
[[index2word[w] for w in line] for line in test]

for line in test:
    for w in line:
        print("{} ".format(index2word[w]), end="")
    print("")
