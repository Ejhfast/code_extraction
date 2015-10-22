# How to find how many ips are pinged on a particular date?
grep "\[07/Mar/2012" logfile.txt | cut -d " " -f 1 | sort | uniq
