# A complex transformation of a data set in pandas
final = pd.DataFrame()
final['team values'] = pdf['Year'].astype('str') + '_' + pdf['Wteam'].astype('str') + '_' + pdf['lteam'].astype('str')
final['predicted_value'] = 1
