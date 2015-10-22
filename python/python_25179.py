# UnicodeEncodeError is occurring while extracting Twitter data
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')
sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer, 'strict')
