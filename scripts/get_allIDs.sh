for family in `ls ..|grep fam_`; do
    cat "../"$family"/"${family:4}"_refIDs" > "../"$family"/"${family:4}"_allIDs";
    cat "../"$family"/"${family:4}"_list_ID" >> "../"$family"/"${family:4}"_allIDs";
    echo ${family:4}" done"
done