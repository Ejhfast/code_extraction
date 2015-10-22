# launching vs2008 build from python
compileit.cmd
  call C:\Program Files\Microsoft Visual Studio 9.0\VC\vcvarsall.bat
  devenv $1.sln /rebuild Debug /Out last-build.txt
