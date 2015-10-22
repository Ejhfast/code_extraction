# What is the correct way of passing parameters to stats.friedmanchisquare based on a DataFrame?
a = np.array([[1, 2, 3], [2, 3, 4] ,[4, 5, 6]])
friedmanchisquare(*(a[i, :] for i in range(a.shape[0])))
