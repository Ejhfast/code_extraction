# How to get batch to run a python script on windows 8
@echo off
start /b "" "%ProgramFiles%\Python33\python.exe" "%UserProfile%\Test.py" "more parameters"
pause
