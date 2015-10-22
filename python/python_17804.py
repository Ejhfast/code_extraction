# How to get splicing method working with both strings and lists
def function(seq, n):
    return seq[n+1:] + seq[n:n+1] + seq[:n]
                       ^^^^^^^^^^
