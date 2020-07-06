for family in `ls ..|grep fam_`; do
    # python3 change_pair_format.py "../"$family"/"${family:4}"_pair_tc" "../"$family"/"${family:4}"_pair_tc.newformat";
    # python3 change_pair_format.py "../"$family"/"${family:4}"_pair_sp" "../"$family"/"${family:4}"_pair_sp.newformat";
    # python3 change_avg_format.py "../"$family"/"${family:4}"_avg_tc" "../"$family"/"${family:4}"_avg_tc.newformat";
    python3 change_avg_format.py "../"$family"/"${family:4}"_avg_sp" "../"$family"/"${family:4}"_avg_sp.newformat";
    python3 change_pairwiseID_format.py "../"$family"/"${family:4}"_pairwiseID" "../"$family"/"${family:4}"_pairwiseID.newformat";
    echo ${family:4}" done";
done