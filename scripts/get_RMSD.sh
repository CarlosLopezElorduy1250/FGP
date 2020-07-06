for family in `ls .. | grep fam_`; do
    python get_RMSD.py "../"$family"/"${family:4}"_RMSD" ${family:4} "../"$family"/"${family:4}"_RMSD.newformat";
    echo ${family:4}" done"
done