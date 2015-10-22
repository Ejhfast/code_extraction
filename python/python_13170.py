# Matching two almost similar string (python)
left,right = a.split('=', 1)
answer = left.split('::')[1:] + [right]
