# how to use pkgutils.get_data with csv.reader in python?
csvdata = pkgutil.get_data("curve", "ntc.10k.csv")
csvio = StringIO(csvdata)
raw = csv.reader(csvio)
