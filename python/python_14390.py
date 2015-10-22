# How can I reindex a series created through the collapsing of a DataFrame?
s = pd.concat([df[i] for i in df], ignore_index = True)
