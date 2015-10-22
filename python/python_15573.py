# Rpy2: How to convert list of dictionaries to R data frame
df = robjects.DataFrame(obs[0])
for ob in obs[1:]:
    df = df.rbind(robjects.DataFrame(ob))
