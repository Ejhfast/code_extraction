# I'm trying to search a '.class' file within jar files using Python
import zipfile
archive = zipfile.ZipFile('&lt;path to jar file&gt;/test.jar', 'r')
list = archive.namelist()
