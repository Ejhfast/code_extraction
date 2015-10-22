# How to copy an object without referencing to it?
run = pymzml.run.Reader(file_to_read, MS1_Precision = 5e-6, MSn_Precision = 20e-6)
  for spec in run:
   tmp = spec.deRef()
