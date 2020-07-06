module use /software/as/el7.2/EasyBuild/CRG/modules/all;
module load Python/2.7.11-foss-2016a;
echo "=== Computing avg SoP with knn ===";
for family in `ls .. | grep fam_`; do
    if [ ! "$family" = "fam_ins" ] && [ ! "$family" = "fam_HLH" ]; then
        #python knn_HOMFAM_avg.py "../"$family"/"${family:4}"_refIDs" "../"$family"/"${family:4}"_avg_tc.newformat" "../"$family"/"${family:4}"_pairwiseID.newformat" 3 "../predictions/"${family:4}"_avg_tc_3_pred";
        python knn_HOMFAM_avg.py "../"$family"/"${family:4}"_refIDs" "../"$family"/"${family:4}"_avg_sp.newformat" "../"$family"/"${family:4}"_pairwiseID.newformat" 3 "../predictions/"${family:4}"_avg_sp_3_pred";
        echo ${family:4}" done"
    fi
done
