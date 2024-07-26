#!/usr/bin/env python3
import sys

fasta = sys.argv[1]
file = f"{fasta}.maf.fa"
outfile = f"{fasta}.maf.rmGap.fa"
per = 0.8

def readFasta(path):
    count = 0
    seqnames, seqs = [], []
    Loading = ["\\","\\","|", "|","/", "/", "-", "-"]
    with open(path) as FILE:
        seq = ""
        for line in FILE:
            line = line.strip()
            if line.find(">") != -1:
                if seq != "":
                    seqnames.append(seqname)
                    seqs.append(seq)
                    seq = ""
                seqname = line
                count += 1
                print(f"[{Loading[count % 8]}]", end = "\r")
                if count % 100 == 0 or count == 1:
                    print("   Loading",count, f"sequences from {path}", end = "\r")
            else:
                seq += line
    print("   Loading",count, f"sequences from {path}", end = "\r", flush = True)
    print(f"[*]", end = "\r", flush = True)
    seqnames.append(seqname)
    seqs.append(seq)
    print()
    return seqnames, seqs

seqnames, seqs = readFasta(file)

remove_sites = []
for i in range(len(seqs[0])):
    current_site_dict = {}
    for k in range(len(seqs)):
        nucl = seqs[k][i]
        current_site_dict.setdefault(nucl, 0)
        current_site_dict[nucl] += 1
    
    if '-' in current_site_dict:
        if current_site_dict['-']/len(seqs) > per:
            remove_sites.append(i)

with open(outfile, 'w') as OUT:
    for i in range(len(seqs)):
        seq = list(seqs[i])
        print("1..", end="", flush=True)
        seq = dict(enumerate(seq))
        print("2..", end="", flush=True)
        new_seq = ""
        # for site in sorted(list(seq.keys())):
        #     if site not in remove_sites:
        #         new_seq += seq[site]
        for key in remove_sites:
            seq.pop(key, None)
        print("3..", end="", flush=True)
        for site in sorted(list(seq.keys())):
            new_seq += seq[site]
        print("4..", end="", flush=True)     
        OUT.write(seqnames[i] + "\n")
        OUT.write(new_seq + "\n")
        print("5", flush=True)
            


