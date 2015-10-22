# How can you extract all 6 letter Latin words to a list?
egrep "^\w{6}$" /usr/share/dict/words | egrep "(.)(.)(.)\3\2\1"
