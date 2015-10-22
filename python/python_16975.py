# How to split a huge file into smaller files alphabetically?
awk '{ print &gt;&gt; "artists_"toupper(substr($1, 1, 1))".txt" }' &lt; songs.txt
