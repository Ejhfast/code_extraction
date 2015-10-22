# Extra character in Python character count (Fedora, Gedit)
truncate -s $(($(wc -m myfile | cut -d' ' -f1)-1)) myfile
