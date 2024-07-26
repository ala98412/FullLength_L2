#!/usr/bin/env bash

genome=$1
fasta=$2

/home/why/Tools/TE_ManAnnot/bin/make_align_from_blast.sh \
	$genome $fasta 0 500
