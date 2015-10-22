# Get rid of the Python launcher icon - OS X
sudo defaults write /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/Info "LSUIElement" -string "1"
