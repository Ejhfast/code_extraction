# Strip leading 'u' from JSON for PHP
$json = str_replace("u'", "'", $json);
$json = str_replace("'", '"', $json);
