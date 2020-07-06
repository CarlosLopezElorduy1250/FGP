rm ../all_knnOutputs_avg_sp_HOMFAM;
touch ../all_knnOutputs_avg_sp_HOMFAM;
echo "=== Mixing all knn outputs into a single file ===";
for family in `ls ..| grep fam_`; do
    if [ ! "$family" = "fam_ins" ] && [ ! "$family" = "fam_HLH" ]; then
        head -n -4 "../predictions/"${family:4}"_avg_sp_3_pred" | tail -n +2 >> ../all_knnOutputs_avg_sp_HOMFAM;
        echo ${family:4}" done";
    fi
done