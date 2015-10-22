# Creating a zero-filled pandas data frame
d = pd.DataFrame(0, index = np.arange(len(data)), columns = feature_list)
