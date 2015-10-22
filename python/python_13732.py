# Bash erases the output file before executing the command
program.py &gt; tmp.csv &amp;&amp; mv tmp.csv file.csv
