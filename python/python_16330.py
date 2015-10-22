# variable number of numpy array for loop arguments required to match variable column numbers
date_objects = np.array([datetime.datetime.strptime(row[0] + row[1], "%Y-%m-%d%H:%M")
                    for row in arr])
