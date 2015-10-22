# What is the best, python or bash for selectively concatenating lots of files?
ls data[0-9]*txt|sort -nk1.5|awk 'BEGIN{rn=5;i=1}{while((getline _&lt;$0)&gt;0){print _ &gt;"data_new_"i".txt"}close($0)}NR%rn==0{i++}'
