#!/usr/bin/env python3

sample = "L2-family-562.fa"
file = f"./{sample}/{sample}.maf.rmGap.trim.fa"
out = f"./{sample}/{sample}.maf.rmGap.trim.sorted.fa"

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

seqs_tuple = []
for i in range(len(seqs)):
    seqs_tuple.append((seqnames[i], seqs[i], len(seqs[i].replace("-", ""))))
seqs_tuple = sorted(seqs_tuple, key=lambda length: length[2], reverse=True)
with open(out, 'w') as FILE:
    for i in range(len(seqs_tuple)):
        FILE.write(f"{seqs_tuple[i][0]}\n")
        FILE.write(f"{seqs_tuple[i][1]}\n")