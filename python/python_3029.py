# Convert Z-score (Z-value, standard score) to p-value for normal distribution in Python
p_values = scipy.stats.norm.sf(abs(z_scores)) #one-sided
