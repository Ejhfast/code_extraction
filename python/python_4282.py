# How can I selectively suppress certain error messages that follow a certain pattern?
python my_program.py 2&gt;&amp;1| grep -v "GLib-GIO-CRITICAL"
