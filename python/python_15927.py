# Capture jpgs produced in subprocess in main script
import subprocess
params = ['convert', 'pdf_file', 'jpg:-']
image_data = subprocess.check_output(params)
