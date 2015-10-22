# How to find text between two markers
print("".join(re.findall(r'\^\[#n(.*?)\$,s\)', string)))
