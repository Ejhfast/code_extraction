# Passing parameters from Python to a makefile
call([path_to_gmake, MAKEFILE]+argv[1:5])
