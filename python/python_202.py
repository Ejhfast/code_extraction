# Is there a fast way to generate a dict of the alphabet in Python?
import string
d = dict.fromkeys(string.ascii_lowercase, 0)
