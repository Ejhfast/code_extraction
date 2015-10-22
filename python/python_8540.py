# PHP Calling Server Scripts - WILL NOT CONTINUE after call
exec('nohup python /home/process/script.py -i '.escapeshellarg($location).' &amp;&gt;/dev/null &amp;');
