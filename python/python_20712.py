# Remove words that appear in other column, Pandas
x['C'] = x['B'].replace(to_replace=r'\b'+x['A']+r'\b', value='',regex=True)
