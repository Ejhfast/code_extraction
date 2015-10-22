# repeat data in the empty lines untill a non-empty line occurs
awk 'NF&gt;3{a=$1;b=$2;c=$3;$1=$1;print;next}NF&lt;3{d=$1;e=$2;print a,b,c,d,e;next}{$1=$1;}1' OFS=',' file
