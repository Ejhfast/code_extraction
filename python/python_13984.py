# How to specify xml output for nose programatically
noseargs = ['foo', '--with-xunit', '--xunit-file=output.xml', '--tests=mytest']
nose.run(argv=noseargs)
