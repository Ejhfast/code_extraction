# Compare Two Dictionaries - Floating Point
def is_equal(floats_a, floats_b, precision=1e-15):
    return all((abs(a-b) &lt; precision) for a, b in izip(floats_a, floats_b))
