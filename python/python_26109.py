# pandas equivalent of cbind
test3 = pd.concat([test1, test2], axis=1)
test3.columns = ['a','b']
