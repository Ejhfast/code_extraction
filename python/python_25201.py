# how to truncate file by number of characters in a specific column
awk -F ';' 'length($3)&lt;10000 &amp;&amp; length($4)&lt;10000' file
