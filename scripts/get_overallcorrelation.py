import sys
from scipy.stats.stats import pearsonr

def correlation(knnOut_path):
    with open(knnOut_path) as knnOut_file:
        real, predicted=[],[]
        if "avg" in knnOut_path:
            for line in knnOut_file.readlines():
                line=line.split("\t")
                real.append(float(line[1]))
                predicted.append(float(line[2]))
        else:
            for line in knnOut_file.readlines():
                line=line.split("\t")
                real.append(float(line[2]))
                predicted.append(float(line[3]))
    corr=pearsonr(real,predicted)
    if "avg" in knnOut_path:
        if "tc" in knnOut_path:
            print("tc\tavg\t"+str(corr[0])+"\t"+str(corr[1]))
        else:
            print("sp\tavg\t"+str(corr[0])+"\t"+str(corr[1]))
    else:
        if "tc" in knnOut_path:
            print("tc\tpair\t"+str(corr[0])+"\t"+str(corr[1]))
        else:
            print("sp\tpair\t"+str(corr[0])+"\t"+str(corr[1]))
    return corr

if __name__=="__main__":
    knnOut_path = sys.argv[1]
    correlation(knnOut_path)
