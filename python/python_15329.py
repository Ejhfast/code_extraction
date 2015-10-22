# What is the fastest way to execute Python from PHP?
$result = popen('python yourscript.py ' . $args, 'r');
