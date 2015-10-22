# python - ignore directory in os.listdir()
runbooksrc_files = [i for i in os.listdir(runbooksrc) if not os.path.isdir(i)]
