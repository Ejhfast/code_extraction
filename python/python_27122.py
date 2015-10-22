# execute the python program on a webpage and display output
$command = escapeshellcmd('/usr/custom/test.py');
$output = shell_exec($command);
echo $output;
