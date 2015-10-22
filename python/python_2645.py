# How to convert comma-separated key value pairs into a dictionary using lambda functions
s = "fname:John,lname:doe,mname:dunno,city:Florida"
sd = dict(u.split(":") for u in s.split(","))
