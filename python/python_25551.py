# How to print selected columns from grep using awk
awk -F"[][, ]" '{a=$2","$3","$4;for (i=5;i&lt;=NF;i++) if($i~/^1(09|10|50|67)=/) a=a","$i;print a}' file
2014-12-22,10:39:54,668,109=5313F,110=Y,150=D,167=CS
