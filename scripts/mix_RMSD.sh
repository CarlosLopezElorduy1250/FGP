rm ../all_RMSD;
touch ../all_RMSD;
echo -e "#sequence\tfamily\tiRMSD\tNiRMS" >> ../all_RMSD;
for family in `ls .. | grep fam_`; do
    tail --lines=+2 "../"$family"/"${family:4}"_RMSD.newformat" >> ../all_RMSD;
    echo ${family:4}" done"
done