# Auto-escape special characters in vimscript
cmd = """let @" = '%s'""" % str(myString).replace("'", "''")
