# How can I change name of arbitrary columns in pandas df using lambda function?
os_list = ['osxx', 'centos', 'windowsx']
df.rename(columns=lambda x: x+'x' if x in os_list else x)
