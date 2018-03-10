from HMM import *
from our_utilities import *
#import sys


sonnets, word2syll, word2index, index2word = loadsonnets()

hmmfiles = ["HMM_32_1000_09101554.txt" ]  #sys.argv[1:]

HMMs = []
for hmmfile in hmmfiles:
    HMMs.append(readHMM(hmmfile))


print(len(HMMs))
all_poem = []
for HMM in HMMs:
    X,Y = HMM.generate_emission(4000)
    line=[]
    poem = []
    syll_counter = 0
    line_counter = 0
    for w in X[-1000:]:
        if syll_counter >= 10 and line_counter <14:
            print('line number')
            print(line_counter)
            print('syllables')
            print(syll_counter)
            print(' '.join(line))
            poem.append(' '.join(line))
            line = []
            line_counter = line_counter + 1
            syll_counter = 0
        else:
            if index2word[w] != '\\':
                line.append(index2word[w])
                syll_counter = syll_counter + int(word2syll[index2word[w]][-1][-1])        
    print('end of sonnet')
    all_poem.append(poem)
print('============================================================================')
print('============================================================================')
for i in range(0,len(all_poem)):
    print(hmmfiles[i][4:6])
    for j in range(0,len(all_poem[i])):
        if j == 3 or j == 7 or j==11 :
            print(all_poem[i][j])
            print('')
        else:
            print(all_poem[i][j])
    print('========================================================================')
    print('========================================================================')
