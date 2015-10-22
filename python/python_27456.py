# "None" in legend pandas python
df = pd.read_excel('filename.xlsm')
df.set_index(keys= ['index_col'], inplace=True)
df['col_to_plot'].plot(legend = True)
