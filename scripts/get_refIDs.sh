for family in `ls .. | grep fam_`; do
    python3 get_refIDs.py "../"$family"/"${family:4}"_ref.fasta" > "../"$family"/"${family:4}"_refIDs"
done