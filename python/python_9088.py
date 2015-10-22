# outputting a list in order of shortest word to longest word (python)
l = ["My", "turtle", "is", "old"]
l.sort(key=len, reverse=True)
# -&gt; ['turtle', 'old', 'My', 'is']
