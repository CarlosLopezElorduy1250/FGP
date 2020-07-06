echo "=== SoP prediction with leaveoneout ===";
for family in `ls ..|grep fam_`; do
    if [ ! "$family" = "fam_ins" ] && [ ! "$family" = "fam_HLH" ]; then
		python leaveoneout.py "../"$family"/"${family:4}_pair_sp "../"$family"/"${family:4}_leaveoneout_pred $family
		echo ${family:4}" done"
	fi
done
