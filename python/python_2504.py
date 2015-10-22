# Take user input and put it into a file in Python?
filename = input ("filename: ");
with open (filename, "w") as f:
  f.write (input ());
