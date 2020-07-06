import sys

# Gets FASTAs of the aligned reference sequences from their alignment.

def write_fastas(alignment_file, output_file):
    with open(alignment_file) as alignment:
        with open(output_file,"w+") as output:
            currentID=""
            for line in alignment.readlines():
                if line[0]==">":
                    output.write(line)
                else:
                    currentFASTA=""
                    for character in line:
                        if character!="-":
                            currentFASTA+=character
                    output.write(currentFASTA)

if __name__=="__main__":
    refalig_file=sys.argv[1] # fam_*****/*****_ref.vie
    fasta_out   =sys.argv[2] # fam_*****/ref_fasta.out

    # refalig_file="fam_*****/*****_ref.vie"
    # fasta_out   ="fam_*****/ref_fasta.out"

    write_fastas(refalig_file, fasta_out)
