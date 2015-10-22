# Create a dummy variable by personid
df['newpers'] = df.personid != df.personid.shift(1)
