# Add 4th column when first 3 columns are identical
$ awk '{a[$1FS$2FS$3]+=$4}END{for(k in a)print k,a[k]}' file
chr2 10500 25700 175
chr1 241783 286397 158
