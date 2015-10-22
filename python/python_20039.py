# How do I slice a pandas dataframe based on a condition?
frioMurteira = data.loc[(data["POM"] == "Murteira") &amp; (data["TMP"] &gt; 7.2), ["DTM","TMP"]]
