# Get and Set X11 clipboard(s) in Linux
xclip -o | sed 's/^./\U&amp;/g' | xclip -i
