from HMM import *
from our_utilities import *

sonnets, word2syll, word2index, index2word = loadsonnets()

observations = word2index

# Compute L and D.
n_states = 4
L = n_states
D = len(observations)

# Randomly initialize and normalize matrices A and O.
A = [[random.random() for i in range(L)] for j in range(L)]

for i in range(len(A)):
    norm = sum(A[i])
    for j in range(len(A[i])):
        A[i][j] /= norm

# Randomly initialize and normalize matrix O.
O = [[random.random() for i in range(D)] for j in range(L)]

for i in range(len(O)):
    norm = sum(O[i])
    for j in range(len(O[i])):
        O[i][j] /= norm

# Train an HMM with unlabeled data.
HMM = HiddenMarkovModel(A, O)
#HMM.unsupervised_learning(X, N_iters)

HMM.X_dict = word2index

writeHMM(HMM)
readHMM('copy and paste from the terminal')
