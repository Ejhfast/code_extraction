# Python Regular expression repeat
x = "--x123-09827--x456-9908872--x789-267504"
p = "--x(?:[0-9]+)-(?:[0-9]+)"
print re.findall(p,x)
