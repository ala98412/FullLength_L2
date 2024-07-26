#!/usr/bin/env bash

genome=$1
sample=$2

mkdir $sample
cd $sample
cp ../run_make_align_from_blast.sh ./
cp ../removeGaps.py ./
ln -s ../L2s/$sample ./

bash ./run_make_align_from_blast.sh ../$genome ./$sample
python3 ./removeGaps.py $sample
