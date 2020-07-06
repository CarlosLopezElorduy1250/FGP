for family in `ls .. | grep fam_`; do
    cd "../"$family;
    touch ${family:4}"_RMSD";
    t_coffee -other_pg irmsd ${family:4}"_ref.vie" -template_file ${family:4}"_ref.template_list" -io_format s >> ${family:4}"_RMSD"
done
cd ../scripts;