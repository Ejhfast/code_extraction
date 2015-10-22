# Feedback on implementation of function which compares integer signs in Python
def all_same_sign(ints):
    return all(x &lt; 0 for x in ints) or all(x &gt; 0 for x in ints)
