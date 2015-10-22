# Python & Pandas: How to do conditional calculation
df['degree'] = df['degree'].apply(lambda x: x + 360 if x &lt; 0 else x)
