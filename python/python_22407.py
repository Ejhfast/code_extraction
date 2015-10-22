# Sqlite3 with python inserting same row
con.execute("Update ansible_packagelist Set upgradeable_version = ? Where package_name = ?", (pkg.candidate.version, package_name))
