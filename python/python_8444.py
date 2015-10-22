# Python subprocess.check_output parsing error
["sqlite3 ", " -separator ',' ", dbLocation, "SELECT blah from argh"] # yours
["sqlite3", "-separator", ",", dbLocation, "SELECT blah from argh"] # mine
