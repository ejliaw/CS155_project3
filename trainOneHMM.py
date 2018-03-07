import our_utilities
from HMM import unsupervised_HMM
import sys

n_hidden = int(sys.argv[1])

n_epochs = int(sys.argv[2])

sonnets, word2syll, word2index, index2word = loadsonnets()

HMM = unsupervised_HMM(sonnets, n_hidden, n_epochs)

writeHMM(HMM, filename=None)
