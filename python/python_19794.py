# Float calculation always off by 1
def area2(n, side):
    r = 0.5 * side * (math.cos(math.pi / n) / math.sin(math.pi / n))
    return n * r * r * math.tan(math.pi / n)
