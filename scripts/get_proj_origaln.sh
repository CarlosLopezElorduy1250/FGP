for family in `ls .. | grep fam_`; do
    t_coffee -other_pg seq_reformat -in "../results/alignments/"${family:4}".dpa_1000.CLUSTALO.with.CLUSTALO.tree.aln" -action +extract_seq_list "../"$family"/"${family:4}"_refIDs" +upper > "../"$family"/"${family:4}"_proj_origaln";
    echo ${family:4}" done";
done