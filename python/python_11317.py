# Python dict incomprehension
{ str(x):(x if x % 2 else x*10) for x in range(10) }
