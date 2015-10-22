# Python: determine actual current module (not __main__)
return os.path.splitext(os.path.basename(__main__.__file__))[0]
