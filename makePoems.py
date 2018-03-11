from HMM import *
from our_utilities import *
#import sys


sonnets, word2syll, word2index, index2word = loadsonnets()

# make syllable dictionaries for end of line and middle of lines.
word2syllEnd = {}
word2syllMiddle = {}
for i in word2syll:
    word2syllMiddle[i] =[]
    for j in range(len(word2syll[i])):
        if word2syll[i][j][0] == 'E':
            word2syllEnd[i]=list(word2syll[i][j])
        else:
            word2syllMiddle[i].append(word2syll[i][j])

for i in word2syll:
    if i not in word2syllEnd:
        word2syllEnd[i]=word2syll[i]
        
for i in word2syllEnd:
    if word2syllEnd[i][0] =='E':
        word2syllEnd[i] = int(word2syllEnd[i][1])
    else:
        val = 0
        for j in range(len(word2syllEnd[i])):
            val = val + int(word2syllEnd[i][j])/len(word2syllEnd[i])
        word2syllEnd[i] = val
for i in word2syllMiddle:
    val = 0
    for j in range(len(word2syllMiddle[i])):
        val = val + int(word2syllMiddle[i][j])/len(word2syllMiddle[i])
    word2syllMiddle[i] = val
        
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
        elif index2word[w] != '\\':
            if syll_counter + word2syllMiddle[index2word[w]]> 10:
                line.append(index2word[w])
                syll_counter = syll_counter + int(word2syllEnd[index2word[w]])        
            else: 
                line.append(index2word[w])
                syll_counter = syll_counter + int(word2syllMiddle[index2word[w]]) 
                
            
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
