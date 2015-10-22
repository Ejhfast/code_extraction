# How to build and fill pandas dataframe from for loop?
d = df[[p, p.team, p.passing_att, p.passer_rating()] for p in game.players.passing()]
