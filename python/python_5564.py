# Write a list of Complex Numbers as Binary Data
flattend = [f for sublist in ((c.real, c.imag) for c in complex_list) for f in sublist]
