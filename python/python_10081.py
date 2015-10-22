# How can I remove duplicate letters in strings?
re.sub(r'(\w)\1+', r'\1', 'yeeeesssss')  // yes
