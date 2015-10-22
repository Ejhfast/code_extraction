# Get actual disk space
os.walk exclude .svn folders
for root, subFolders, files in os.walk(rootdir):
    if '.svn' in subFolders:
      subFolders.remove('.svn')
