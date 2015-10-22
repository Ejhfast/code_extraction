# subprocess.check_output failing with error 127
p = subprocess.Popen(["/path/to/casperjs", "casper.js", startUrl, row[0]], env={"PATH": "/path/to/phantomjs"})
url, err = p.communicate()
