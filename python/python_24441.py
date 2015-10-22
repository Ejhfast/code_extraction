# Python: create multiple boxplots in one pannel
savelist = [data[label == 1]]
for i in [2,3,4,5]:
    savelist.append(data[label == i])
