# keep open windows console after a python syntax error
C:\Python26\python.exe %1
IF %ERRORLEVEL% NEQ 0 PAUSE
