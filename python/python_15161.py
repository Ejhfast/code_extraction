# py2exe / cx_Oracle - OCI.dll in the resulting dist
options={"py2exe" : {"dll_excludes": ["OCI.dll",], "includes" : ["decimal", ]}})
