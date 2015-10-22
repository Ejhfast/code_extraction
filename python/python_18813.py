# define an integration function in python
X = [0.1*i for i in xrange(40)]
Y = [TotalEnergy_GW_onelevel(x) for x in X]
plot(X,Y)
