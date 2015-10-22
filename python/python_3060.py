# how to 'marry' two strings in python?
def mix(s, c=' ', n=1):
    return ''.join(s[i:i+n]+c for i in range(0,len(s),n))
