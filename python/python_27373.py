# Count most frequent 100 words from sentences in Dataframe Pandas
Counter(" ".join(df["text"]).split()).most_common(100)
