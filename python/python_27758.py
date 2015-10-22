# Creating pandas DataFrame from numpy array leads to strange errors
d = fits.getdata('data.fit')
df=pd.DataFrame(np.array(d).byteswap().newbyteorder())
