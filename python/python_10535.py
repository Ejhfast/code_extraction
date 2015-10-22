# python: removing first instance of a specific character using regex
s = '| | +-out\windows-x86-MD-mbcs-vs2008-rel\bin\VisualStudio08-32bit.exe'
print s.split('-', 1)[1]
# out\windows-x86-MD-mbcs-vs2008-relin\VisualStudio08-32bit.exe
