# Run Python script from php, save process pid, and don't wait it to finish
$a = exec('python myScript.py &gt; /dev/null 2&gt;&amp;1 &amp; echo $!');
 echo $a;
