# Pandas: divide each row by another row depending on the index
df_daily = df[df["Date"].hour == 16].copy().shift(1)
df = df.join(df_daily, rsuffix="closing_").fillna(method="ffill")
