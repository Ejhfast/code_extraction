# Renaming all files in a folder based on the filenames they already have
filename = os.path.join("C:\path\to\Sales Packs", filename)
os.rename(filename, filename[0:11]+accName+".xlsx")
