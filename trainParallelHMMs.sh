homedir="$1"
datadir="$homedir/data"

nepochs=1000

cd $homedir

for L in 1 2 4 8 12 16; do
    python trainOneHMM.py $L $nepochs &
done
