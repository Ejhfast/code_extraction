# automating android CTS with python
cts_tradefed_script = "./android-cts/tools/cts-tradefed"
process = subprocess.Popen([cts_tradefed_script + " " + serialno], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
