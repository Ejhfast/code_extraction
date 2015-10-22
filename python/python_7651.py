# call python from php
$output = array();
exec("python hi.py", $output);
var_dump( $output);
