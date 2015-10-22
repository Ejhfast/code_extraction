# Removing a small number of lines from a large file
grep -vP "[\x80-\xFF]" data.tsv &gt; data-ASCII-only.tsv
