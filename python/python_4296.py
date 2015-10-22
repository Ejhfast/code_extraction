# Python IndexError when trying to go through a large list
LOG_FILES = [LogFile(f) for f in glob.glob(srcdir + "/*.txt")
                        if from_date &lt;= f.DATE &lt;= to_date]
