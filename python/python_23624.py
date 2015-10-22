# Quickest way to get number of lines in a file
0.024 sec (avg) - wc -l file.txt
0.121 sec (avg) - sed -n '$=' file.txt
0.396 sec (avg) - nl file.txt | tac |sed -n 1p | awk '{print $1}
