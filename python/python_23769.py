# how do i export PDF file attachments via python
from subprocess import call
call(["pdfdetach", "-saveall", "file.pdf"])
