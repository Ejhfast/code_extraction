# How to set a timeout for gurobi using python
m = gurobipy.model()
m.setParam('TimeLimit', 5*60)
