# Accept track changes and convert .doc to .txt using CATDOC
(fi, fo, fe) = os.popen3('antiword -f "%s"' % filename)
