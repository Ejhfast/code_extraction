# Give column name when read csv file pandas
colnames=['TIME', 'X', 'Y', 'Z']
user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)
