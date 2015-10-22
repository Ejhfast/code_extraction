# c++ python 3 binding
wchar_t progname[FILENAME_MAX + 1];
mbstowcs(progname, argv[0], strlen(argv[0]) + 1);
Py_SetProgramName(progname);
