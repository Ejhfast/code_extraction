# python for loop with updated values
for i in range(1,len(DF)):
    DF.iloc[i]['b'] = DF.iloc[i-1]['b']+DF.iloc['i']['c']
