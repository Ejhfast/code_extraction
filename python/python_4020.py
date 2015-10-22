# What is the right way to add an `if` to a generator expression in Python?
s = ''.join('%s: %s &lt;/br&gt;' %
               (a,getattr(user, a)) for a in dir(user) if '__' not in a
           )
