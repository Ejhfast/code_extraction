# Convert function to single line list comprehension
multiples[:] = [n for i,n in enumerate(multiples)
                       if all(n % small for small in multiples[i+1:])]
