#!/usr/bin/env bash

samples=$(ls ./L2s)
genome=Cb.genome.fa

rm parallel_command.txt

for sample in ${samples[@]}
do
  echo "bash ./main_bash.sh $genome $sample" >> parallel_command.txt
done

parallel -j 10 < ./parallel_command.txt