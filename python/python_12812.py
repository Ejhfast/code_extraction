# Calling Python code from Gnome Shell extension
const Util = imports.misc.util;
let python_script = '/path/to/python/script';
Util.spawnCommandLine("python " + python_script);
