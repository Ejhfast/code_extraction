# counting column values in pandas
dictionary = {'Year': [1985, 1985, 1986, 1986, 1987, 1987, 1987]}
pdf = pd.DataFrame(dictionary)
gb = pdf.groupby('Year')['Year'].count()
