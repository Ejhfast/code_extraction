# Pandas floating point issue with cumsum and division
sales['PERCENT_2012'] = sales['TOTAL_2012'] / sales['TOTAL_2012'].sum()
sales['CUM_PERCENT_2012'] = sales['PERCENT_2012'].cumsum().round(2)
