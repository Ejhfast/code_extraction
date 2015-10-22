# Python: Print the common letter from user input
from collections import Counter
[letter for letter,count in Counter("Thomas Jones").items() if count &gt; 1]
