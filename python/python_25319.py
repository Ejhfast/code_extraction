# Closing file after using to_csv()
outfile = open(path+'filename.csv', 'wb')
df.to_csv(outfile)
oufile.close()
