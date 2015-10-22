# calculate mean or variance for subset of pandas DF column
DF['means']=DF[['A','B','C','D']].mean(axis=1)
