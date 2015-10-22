# how to confine to write a string in specific list ,on google-app-engine
p = db.StringProperty(choices=set(["aa", "bb", "cc"]))
