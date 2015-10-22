# cd into another directory to execute a script
subprocess.call(["java","Autoingestion",self.username, self.password, self.vendor_number, "Sales","Daily","Details",self.date, cwd="sales")
