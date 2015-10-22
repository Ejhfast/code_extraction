# How do I write output in same place on the console?
sys.stdout.write("Download progress: %d%%   \r" % (progress) )
sys.stdout.flush()
