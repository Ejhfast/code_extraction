# quotes within a string
f = r"""awk -F"\t" '{print$5" "$6" "$7}' file.txt | sort | uniq -c"""
