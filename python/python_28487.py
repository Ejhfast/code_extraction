# What's the most efficient way to filter values out of a list based on the values in another list
res = [word for word in simpleTokenize(string) if word not in stopwords]
