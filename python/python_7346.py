# Writing to a new directory in Python without changing directory
dir_path = os.path.join(self.feed, self.address)  # will return 'feed/address'
os.makedirs(dir_path)                             # create directory [current_path]/feed/address
output = open(os.path.join(dir_path, file_name), 'wb')
