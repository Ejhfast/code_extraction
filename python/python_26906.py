# Changing data type with pandas on read_excel
df["DEPS"]=df["DEPS"].map(lambda x:'{0:03d}'.format(int(x)))
