# extra separator from pandas.to_csv function
new_train[indice_90_percent:].to_csv('test_products.txt',header=True, sep="|", index=False)
