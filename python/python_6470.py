# subprocess.Popen running infinite loop with py2exe
app_path = os.path.realpath(os.path.join(
    os.path.dirname(sys.executable), 'test.exe'))
child = subprocess.Popen(app_path)
