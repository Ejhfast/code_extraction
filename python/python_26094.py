# How can I normalize the data in a range of columns in my pandas dataframe
# Assuming same lines from your example
cols_to_norm = ['Age','Height']
survey_data[cols_to_norm] = survey_data[cols_to_norm].apply(lambda x: (x - x.mean()) / (x.max() - x.min()))
