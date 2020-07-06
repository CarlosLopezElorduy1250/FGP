for family in `ls ..|grep fam_`; do
    python3 get_refFASTAs.py "../"$family"/"${family:4}"_ref.vie" "../"$family"/"${family:4}"_ref.fasta"
done