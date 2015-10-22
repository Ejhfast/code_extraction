# Running a command line from python and piping arguments from memory
import subprocess
out, err = subprocess.Popen(["pdftotext", "-", "-"], stdout=subprocess.PIPE).communicate(pdf_data)
