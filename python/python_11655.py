# Python string LCS bug
if t1[0] &gt; t2[0] or t1[0] == t2[0]:
    return [t1[0], '#'+t1[1], t1[2]]
return [t2[0], t2[1], '#'+t2[2]]
