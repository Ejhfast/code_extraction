# Reading lines from .txt into batch file and handing into command line as arguments?
for /f "usebackq tokens=* delims=" %%# in ("C:\path\to\document.txt") do (
    call "C:/path/to/script.js" %%#
)
