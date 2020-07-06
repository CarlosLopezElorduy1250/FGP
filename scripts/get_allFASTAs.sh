for family in `ls ..|grep fam`; do
    touch "../"$family"/"${family:4}"_allFASTAs.fasta";
    cat "../"$family"/"${family:4}"_ref.fasta" >> "../"$family"/"${family:4}"_allFASTAs.fasta";
    cat "../"$family"/"${family:4}"_test-only.vie" >> "../"$family"/"${family:4}"_allFASTAs.fasta";
    echo ${family:3}" done";
done