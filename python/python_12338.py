# Python Recursion Backtracking Variable
return path(a, row+1, col, weight, list(cumulative)) +
       path(a, row+1, col+1, weight, list(cumulative))
