# How to map a function to a triple nested list and keep the triple nested list intact?
dataset = [[[float(value) for value in measure]
                           for measure in subject]
                           for subject in dataset]
