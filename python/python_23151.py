# Create set of keys from a list of dictionaries
lst = [ {"a":45, "b":2, "c":"house"}, {"a":36, "d":67, "e":"car"} ]
{ k for d in lst for k in d }
=&gt; set(['a', 'c', 'b', 'e', 'd'])
