# Pass multiline html as argument via php system()
$parsedString = system("python replace.py '$replaceString' '$replaceTo' '$source'", $retval);
