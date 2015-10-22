# python split string on whitespace following specific character
import re
a = 'aaaa bbbb cccc:dd eeee:ff ggg hhhh iiii:jjjj kkkk:llll:mm nnn:ooo pppp qqqq:rrr'
print(re.findall(r'([^:]*:[^ ]*) *', a))
