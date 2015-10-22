# Iterating over full text lines instead of characters
for line in open('file'):
    for word in line.split():
        do_stuff(word)
