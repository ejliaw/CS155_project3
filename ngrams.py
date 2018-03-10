from HMM import *
from our_utilities import *

sonnets, word2syll, word2index, index2word = loadsonnets()

nwords = len(word2index.keys())
n = 3

laplacianSmoothing = 0 #1.0 / (nwords**(n-1))
jointprob = np.zeros( (nwords,)*(n) )
jointprob = jointprob + laplacianSmoothing

for sonnet in sonnets:
    length = len(sonnet)
    for i in range(length - n):
        ngram = sonnet[i:i+n]
        #prevs = ngram[:-1]
        #output = ngram[-1]
        jointprob[tuple(ngram)] += 1

#normsum = np.sum(jointprob)
#jointprob = jointprob / normsum

normsum = np.sum(jointprob, axis=-1)
jointprob = jointprob / np.expand_dim(normsum, n-1)

seedsentence = "shall i" #compare"
seed = [word2index[word] for word in seedsentence.split()]

how_sparse_debug = 0

newsonnet = []
n_syllables = 0
prevs = seed[:-1]
curr = seed[-1]
for line in range(14):
    while n_syllables < 10:
        while True:
            P = jointprob[prevs]
            if np.sum(P) > 0:
                newword = np.random.choice(nwords, 1, p=P)
            else:
                print(prevs)
                how_sparse_debug += 1
                newword = np.random.choice(nwords, 1)
            newsonnet.append(newword)
            new_syllables = int(word2syll[newword][1][-1])
            n_syllables += new_syllables
            if n_syllables > 10:
                del newsonnet[-1]
                n_syllables -= new_syllables
            else:
                prevs = prevs[1:] + [newword]
                break 











hmmfiles = ["HMM_1_1000_08174814.txt", "HMM_2_1000_08175333.txt" ]  #sys.argv[1:]

HMMs = []
for hmmfile in hmmfiles:
    HMMs.append(readHMM(hmmfile))


print(len(HMMs))
all_poem = []
for HMM in HMMs:
    xs, ys = HMM.generate_emission(400)
    line=[]
    poem = []
    syll_counter = 0
    line_counter = 0
    for w in xs:
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
                syll_counter = syll_counter + int(word2syll[index2word[w]][0][-1])        
    print('end of sonnet')
    all_poem.append(poem)
print('============================================================================')
print('============================================================================')
for i in range(0,len(all_poem)):
    print(hmmfiles[i][4])
    for j in range(0,len(all_poem[i])):
        if j == 3 or j == 7 or j==11 :
            print(all_poem[i][j])
            print('')
        else:
            print(all_poem[i][j])
    print('========================================================================')
    print('========================================================================')
