import os, sys

def leaveoneout(seq2closestneigh,pairseq2sop):
    seq2realsop={}
    seq2predsop={}

    for target in seq2closestneigh.keys():
        realsum=0.0
        predsum=0.0
        ind1, ind2=0,0

        for second_seq in seq2closestneigh.keys():
            if target!=second_seq and second_seq!=seq2closestneigh[target]:
                try:
                    realsum+=pairseq2sop[(target,second_seq)]
                except:
                    realsum+=pairseq2sop[(second_seq,target)]
                ind1+=1
        seq2realsop[target]=realsum/ind1

        pred_target=seq2closestneigh[target][0]
        for second_seq in seq2closestneigh.keys():
            if pred_target!=second_seq and second_seq!=target:
                try:
                    predsum+=pairseq2sop[(pred_target,second_seq)]
                except:
                    predsum+=pairseq2sop[(second_seq,pred_target)]
                ind2+=1
        seq2predsop[target]=predsum/ind2
    return (seq2realsop,seq2predsop)


if __name__ == "__main__":
    original_sop_file=sys.argv[1]
    outfile          =sys.argv[2]
    fam_name         =sys.argv[3]

    '''
    3huda      1cdoa         55.2    97.6 [100.0]   [  746]
    3huda      1teha         62.6    98.1 [100.0]   [  744]
    3huda      2ohxa         87.2   100.0 [100.0]   [  748]
    3huda      1d1ta         69.7   100.0 [100.0]   [  746]
    1cdoa      1teha         62.9    98.9 [100.0]   [  744]
    1cdoa      2ohxa         55.0    97.6 [100.0]   [  746]
    1cdoa      1d1ta         52.7    97.6 [100.0]   [  744]
    1teha      2ohxa         62.1    98.1 [100.0]   [  744]
    1teha      1d1ta         60.9    98.1 [100.0]   [  742]
    2ohxa      1d1ta         70.8   100.0 [100.0]   [  746]
    '''

    seq2closestneigh={}
    pairseq2sop={}
    wrong_seqs={"1bd7a","1bqqm"} # Misleading structures (want to remove them)

    with open(original_sop_file, "r") as original_sop:
        for line in original_sop.readlines():
            line=line.split()
            seq1,seq2,pid,sop = line[0],line[1],line[2],line[3]

            # FILTER TWO MISLEADING STRUCTURES: 1bd7a and 1bqqm
            if seq1 not in wrong_seqs and seq2 not in wrong_seqs:

                # Assign each sequence to its closest neighbor
                if seq1 not in seq2closestneigh.keys():
                    seq2closestneigh[seq1]=(seq2,pid)
                else:
                    if pid>seq2closestneigh[seq1][1]:
                        seq2closestneigh[seq1]=(seq2,pid)
                
                if seq2 not in seq2closestneigh.keys():
                    seq2closestneigh[seq2]=(seq1,pid)
                else:
                    if pid>seq2closestneigh[seq2][1]:
                        seq2closestneigh[seq2]=(seq1,pid)
                
                # Assign the sop of each pair into a dictionary
                pairseq2sop[(seq1,seq2)]=float(sop)

        
    real,pred=leaveoneout(seq2closestneigh,pairseq2sop)

    # Write in output file
    with open(outfile,"w+") as out:
        out.write('#target'+'\t'+'real'+'\t'+'predicted'+'\t'+'dist_cn'+'\t'+'family'+'\n')
        for seq in seq2closestneigh.keys():
            D=abs(real[seq]-pred[seq])
            out.write(str(seq)+'\t'+str(real[seq])+'\t'+str(pred[seq])+'\t'+str(seq2closestneigh[seq][1])+'\t'+fam_name+'\n')
### DEBUG
