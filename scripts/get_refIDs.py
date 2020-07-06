import sys

with open(sys.argv[1]) as ref_fasta:
    for line in ref_fasta.readlines():
        if line[0]==">":
            print(line[:-1])
