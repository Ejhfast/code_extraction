# Is there a numpy builtin to reject outliers from a list
def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) &lt; m * np.std(data)]
