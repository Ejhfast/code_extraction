# Python List Appending
FinalList = [(k, [int(i)*v for i in dr[k]]) for k, v in SimList]
TotalList = [sum(x) for x in zip(*(j for i in FinalList for j in i[1:]))]
