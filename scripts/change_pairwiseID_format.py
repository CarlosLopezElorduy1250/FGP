import sys

def reformat(pairwiseID_file, pairwiseID_reformat):
    with open(pairwiseID_file) as pairwiseID_f:
        with open(pairwiseID_reformat, "w+") as pairwiseID_r:
            for line in pairwiseID_f.readlines():
                line=line.split()
                pairwiseID_r.write(line[4]+" "+line[5]+" "+line[6]+"\n")

if __name__=="__main__":
    pairwiseID_file     = sys.argv[1]
    pairwiseID_reformat = sys.argv[2]

    reformat(pairwiseID_file, pairwiseID_reformat)