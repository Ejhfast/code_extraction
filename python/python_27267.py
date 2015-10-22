# How do I efficiently split all the data in str in python?
s = '1.02.34.35.55.33.64.64.46.74.36.67.45.68.53.75.54.45.23.67.24.98.67.45.23.75.2'
for i in range(0,len(s),3):
    print(s[i:i+3])
