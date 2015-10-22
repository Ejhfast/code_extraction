# Random choice with negative weights
weights = [10, -2, 7]
offset = min(weights)
positiveweights = [z - offset + 1 for z in weights]
