
### !!!!!!! ### You have to replace this with your own current directory.
homedir='/home/ericliaw/CS155/CS155_project3'

#homedir="$1"
datadir="$homedir/data"

nepochs=1000

cd $homedir

#for L in 2; do
for L in 1 2 4 8 12 16; do
    python trainOneHMM.py $L $nepochs &
done
