# GAE/P: mail_stub.get_sent_messages fails with non-ascii since v 1.7.1
Best means of extracting values from the following string in python?
pattern = re.compile(r"\[.*?([0-9]+(?:\.[0-9]+)?).*?\]")
pre, post = [float(x) for x in re.findall(pattern, thestring)]
