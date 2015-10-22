# How can I add integers recursively in Python?
def sumD(num):
    if num == 0: return 0
    return (num % 10) + sumD(num // 10)
