# Preventing dividing by zero in list comprehensions
[confusion_matrix[idx][idx] / sum(confusion_matrix[idx]) if sum(confusion_matrix[idx]) != 0 else 0 for (idx, scores) in enumerate(confusion_matrix)]
