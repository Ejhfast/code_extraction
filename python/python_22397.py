# creating stacked histogram with pandas dataframes data python
plt.hist([df1['text'],df2['printed']], bins=100, range=(1,100), stacked=True, color = ['r','g'])
