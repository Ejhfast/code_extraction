# Python dict: Creating a prepared statement
a=dict(b=3, c='d', x=10)
print ",".join(['{0}=${1}'.format(k, i) for i, k in enumerate(sorted(a))])
