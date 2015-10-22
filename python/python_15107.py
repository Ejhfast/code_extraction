# Copy upper triangle to lower triangle in a python matrix
for i in range(num_rows):
    for j in range(i, num_cols):
        matrix[j][i] = matrix[i][j]
