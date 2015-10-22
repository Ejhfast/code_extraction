# How to extract some numbers from a character string with comma seperating some numbers using python?
x = "1977   1,048.20    1,039.40    894.10  694.70  664.20  1,031.60    928.60  18.80   10:27:05    "
nums = [float(item) if '.' in item else int(item) for item in x.replace(':', ' ').replace(',', '').split()]
print nums #[1977, 1048.2, 1039.4000000000001, 894.10000000000002, 694.70000000000005, 664.20000000000005, 1031.5999999999999, 928.60000000000002, 18.800000000000001, 10, 27, 5]
