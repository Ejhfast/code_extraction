# String manipulation in list of lists in Python
persons = [p[:4]+[p[4].replace('-','').replace('/',''),p[5]] for p in persons]
p4 = [p for p in persons if p[4][-2]=='4']
pblue = [p for p in persons if p[5]=='Blue']
