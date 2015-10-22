# Is there a way to implement sample weights in python logistic regression?
import statsmodels.api as sm
logmodel=sm.GLM(trainingdata[['Successes', 'Failures']], trainingdata[['const', 'A', 'B', 'C', 'D']], family=sm.families.Binomial(sm.families.links.logit)).fit()
