# Plotting one scatterplot with multiple dataframes with ggplot in python
ggplot(aes(x='x', y='y'), data=df1) + geom_point() +
       geom_point(aes(x='x', y='y'), data=df2)
