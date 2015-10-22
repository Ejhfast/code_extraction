# Python replace only part of a re.sub match
re.sub("(?&lt;=[^a-zA-Z])pi(?=[^a-zA-Z])", "(math.pi)", "2pi3 + supirse")
