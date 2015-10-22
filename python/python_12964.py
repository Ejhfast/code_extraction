# Python 2.7/3 C module for working with unicode strings
if (! setlocale(LC_ALL, "ru_RU.utf8")) return PyErr_SetFromErrno(SetLocaleError);
wprintf(L"%ls\n", src);
