# Error running Python script from Applescript
set script_path to "$HOME/Desktop"
do shell script "python " &amp; script_path &amp; "/hello_world.py"
