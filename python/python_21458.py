# Keeping the old value when a division by zero occurs
A = np.where(D != 0, A / D, A)
