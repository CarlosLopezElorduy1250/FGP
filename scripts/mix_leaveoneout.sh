echo "=== Mixing all outputs of leaveoneout in single file ===";
rm ../all_leaveoneout;
touch ../all_leaveoneout;
echo -e "#target\treal_sop\tpredicted_sop\tdist_cn\tfamily">>../all_leaveoneout;

for family in `ls ..|grep fam_`; do
    if [ ! "$family" = "fam_ins" ] && [ ! "$family" = "fam_HLH" ]; then
		tail -n +2 "../"$family"/"${family:4}"_leaveoneout_pred" >> ../all_leaveoneout;
		echo ${family:4}" done"
	fi
done
