# Processing a log to fix a malformed IP address ?.?.?.x
perl -p -i -e 's/\.x/\.7/' foo.log
