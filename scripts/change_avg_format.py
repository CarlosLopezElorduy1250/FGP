import sys

def reformat(avgtc_file, avgtc_reformat):
    with open(avgtc_file, "r") as avgtc_f:
        with open(avgtc_reformat, "w+") as avgtc_r:
            for line in avgtc_f.readlines():
                line=line.split()
                avgtc_r.write(line[0]+"\t"+line[3]+"\n")

if __name__=="__main__":
    avgtc_file     = sys.argv[1]
    avgtc_reformat = sys.argv[2]

    reformat(avgtc_file, avgtc_reformat)