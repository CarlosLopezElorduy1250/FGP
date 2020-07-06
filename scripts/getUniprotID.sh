for family in `ls ..|grep fam_`; do
    python3 getUniprotID.py "../"$family"/"${family:4}"_test-only.vie" "../"$family"/"${family:4}"_list_ID";
    echo ${family:4}" done"
done