echo "=== Computing correlation ===";
for family in `ls ..| grep fam_`; do
    python correlation_avg.py "../all_knnOutputs_avg_sp_HOMFAM" "../fam_"${family:4}"/"${family:4}"_correlation_avg_sp_HOMFAM";
    echo ${family:4}" done";
done