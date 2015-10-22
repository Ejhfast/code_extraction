# Data frame column with conditional data - Python
df["group"][df["pc"] &lt; 0.66] = 2
df["group"][df["pc"] &lt; 0.33] = 1
