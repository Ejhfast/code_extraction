# Regression using PYMC3
pm.glm.glm('y ~ x', data,
           family=pm.glm.families.Normal(priors={'sd': ('sigma', pm.Uniform.dist(0, 12000))}))
