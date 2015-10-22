# call python script *with non-standard library imported* from php
putenv('PYTHONPATH=x');
exec("/home/my_user_name/local/Python-2.7/bin/python test.py", $output, $ret_code);
