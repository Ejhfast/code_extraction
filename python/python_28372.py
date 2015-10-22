# ggplot Bar Plot semantics
ggplot(aes(x='date', y='entries_sum'), data=data) + geom_bar(stat='identity')
