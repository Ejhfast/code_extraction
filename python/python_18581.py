# Specify destination for tarfile
tar = tarfile.open("/backup/output_filename.tar.gz", "w:gz")
tar.add(input)
tar.close()
