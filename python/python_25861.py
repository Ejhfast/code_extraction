# Python Scheduled Task Close taskeng.exe
from os import system
system('taskkill /fi "WindowTitle eq taskeng.exe"')
