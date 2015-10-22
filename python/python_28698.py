# How can I delete the letter that occurs in the two strings using python?
def revers_e(s1, s2):
    print(*[i for i in s1 if i in s2])    # Print all characters to be deleted from s1
    s1 = ''.join([i for i in s1 if i not in s2])    # Delete them from s1
