# Python one-liner to print every file in the current directory
ls -al | python -c "import sys; print sys.stdin.readlines()"
