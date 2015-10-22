# List comprehension and len() vs. simple for loop
sum(1 for word in words if len(word) &gt;= 2 and word[0] == word[-1])
