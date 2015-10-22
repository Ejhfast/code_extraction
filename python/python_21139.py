# How to extract a string from text that is 50 chars long and consists of A to Z and 0-9 .. starts with a capital letter
reobj = re.compile(r"""(?=[A-Z])([A-Za-z0-9"'. ]{50,}\.)""")
result = reobj.findall(subject)
