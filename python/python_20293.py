# is there possible to resolve this star pyramid
stop, first = map(int, raw_input().split())
for i in range(stop - 1):
    print '*' * (i + first)
