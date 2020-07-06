import sys, os
# cwd = os.getcwd()
# os.chdir(cwd+"/scripts")


if __name__ == "__main__":
    RMSD_arg=sys.argv[1]
    family=sys.argv[2]
    out_arg=sys.argv[3]

    iRMSD=""
    NiRMS=""
    current_seq=""

    with open(RMSD_arg,"r") as RMSD_file:
        with open(out_arg,"w+") as out_file:
            out_file.write("#sequence\tfamily\tiRMSD\tNiRMS\n")
            for line in RMSD_file.readlines():
                line=line.split()
                if line!=[] and line[0]=="#AVERAGE":
                    if current_seq!="":
                        out_file.write(current_seq+"\t"+family+"\t"+iRMSD+"\t"+NiRMS+"\n")
                    current_seq=line[3]
                if line!=[] and line[0]=="AVERAGE":
                    if line[1]=="iRMSD:":
                        iRMSD=line[2]
                    if line[1]=="NiRMS:":
                        NiRMS=line[2]
            out_file.write(current_seq+"\t"+family+"\t"+iRMSD+"\t"+NiRMS+"\n")
