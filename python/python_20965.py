# Recursively copy file to a directory all its sub-directory in command prompt
for /d /r "c:\test\" %%a in (*) do copy c:\test.dll "%%~fa"
