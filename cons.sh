#!/usr/bin/env bash

sample=(L2-DR0049120.fa L2-DR0115233.fa L2-DR0126107.fa L2-family-20.fa L2-family-28.fa L2-family-33.fa L2-family-37.fa L2-family-44.fa L2-family-128.fa L2-family-562.fa)

for sample in ${sample[@]}
do
   echo "$sample cons"
   cons -sequence ./$sample/$sample.maf.rmGap.trim.sorted.fa -outseq ./$sample/$sample.maf.rmGap.trim.sorted.cons.fa plurality=1
   echo "$sample getorf"
   getorf -sequence ./$sample/$sample.maf.rmGap.trim.sorted.cons.fa -outseq ./$sample/$sample.maf.rmGap.trim.sorted.cons.orf.fa -minsize 300
   echo "$sample interproscan"
   /home/why/Tools/interproscan-5.55-88.0/interproscan.sh -cpu 10 -f TSV -i ./$sample/$sample.maf.rmGap.trim.sorted.cons.orf.fa -d ./$sample/
done
