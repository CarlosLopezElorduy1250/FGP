touch ../all_correlation
for knnfile in `ls ..|grep all_knnO`; do
    python get_overallcorrelation.py "../"$knnfile >> ../all_correlation;
done