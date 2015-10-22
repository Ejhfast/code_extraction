# Linux - How can I copy files of the same extension located in several subdirectories into a single directly?
find /path/to/src -name "*.nr" -exec cp \{\} /path/to/dest \;
