# Fast algorithm to calculate delta of two list
D = dict((title, rank) for rank, title in enumerate(albums_yesterday))
for rank, title in enumerate(albums_today):
    D[title] = D[title] - rank
