echo "Threshold_dist Cumulative Sample_c" > ../all_correlations_avg_sp;
# echo "Threshold_dist Cumulative Sample_c" > ../all_correlations_avg_tc;
# echo "Threshold_dist Cumulative Sample_c" > ../all_correlations_pair_sp;
# echo "Threshold_dist Cumulative Sample_c" > ../all_correlations_pair_tc;

for family in `ls .. | grep fam_`; do
    tail --lines=+2 "../"$family"/"${family:4}"_correlation_avg_sp_HOMFAM" >> ../all_correlations_avg_sp;
    # tail --lines=+2 "../"$family"/"${family:4}"_correlation_avg_tc_HOMFAM" >> ../all_correlations_avg_tc;
    # tail --lines=+2 "../"$family"/"${family:4}"_correlation_pair_sp_HOMFAM" >> ../all_correlations_pair_sp;
    # tail --lines=+2 "../"$family"/"${family:4}"_correlation_pair_tc_HOMFAM" >> ../all_correlations_pair_tc;
    echo ${family:4}" done"
done