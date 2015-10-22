# Search and replace in current file with Sublime Text plugin
for line in fileinput.input(self.view.file_name(), inplace=1):
  sys.stdout.write(self.makeReplacements(line))
