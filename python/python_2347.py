# building a pairwise matrix in scipy/numpy in Python from dictionaries
result = [[compute_stat(data[row], data[col]) for col in labels]
          for row in labels]
