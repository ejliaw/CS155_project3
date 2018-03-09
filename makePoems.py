from HMM import *
from our_utilities import *
#import sys


sonnets, word2syll, word2index, index2word = loadsonnets()

hmmfiles = ["HMM_1_1000_08174814.txt", "HMM_2_1000_08175333.txt" ]  #sys.argv[1:]

HMMs = []
for hmmfile in hmmfiles:
    HMMs.append(readHMM(hmmfile))


print(len(HMMs))

for HMM in HMMs:
    xs, ys = HMM.generate_emission(120)
    poem = [index2word[w] for w in xs]
    print(poem)
