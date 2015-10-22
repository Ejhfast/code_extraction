# Represent string as an integer in python
num = 0
for ch in my_string:
    num = num &lt;&lt; 8 + ord(ch)
