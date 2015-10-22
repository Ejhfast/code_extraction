# The optimal way to remove duplicates from a list of sorted very large files (200G each)?
cat infile.txt | tr -d " " | uniq &gt; outfile.txt
