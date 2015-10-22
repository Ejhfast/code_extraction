# Python: Regular expression for exactly $n$ [?o], with at least one [o]
re.compile("(?=.{0," + str(n - 1) + "}o)[o?]{" + str(n) + "}")
