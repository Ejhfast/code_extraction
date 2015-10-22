# Longest common subsequence of 3+ strings
dp[i, j, k] = 1 + dp[i - 1, j - 1, k - 1] if A[i] = B[j] = C[k]
              max(dp[i - 1, j, k], dp[i, j - 1, k], dp[i, j, k - 1]) otherwise
