# Get data from cell in pandas and user it in calculations
firstServePecentage = df[df['Player'] == 'Novak Djokovic']['1st Srv']
firstServePecentage.values[0]
