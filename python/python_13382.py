# Finding last occurence of substring in string, replacing that
old_string = "this is going to have a full stop. some written sstuff!"
k = old_string.rfind(".")
new_string = old_string[:k] + ". - " + old_string[k+1:]
