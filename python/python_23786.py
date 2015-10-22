# Splitting strings in python, then joining them into so that each string is one substring longer than the next
s = "-o-pp-gg-s-h"
ss = s.split("-")
series = ["-".join(ss[:x]) for x in range(2,len(ss)+1)]
