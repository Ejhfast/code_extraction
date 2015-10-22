# What is the required compiler to compile sqlalchemy C extensions on Win7 64-bits?
setlocal EnableDelayedExpansion
call "%ProgramFiles%\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" /Release /x64 /vista
set DISTUTILS_USE_SDK=1
