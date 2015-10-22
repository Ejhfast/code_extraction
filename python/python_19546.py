# search and replace enumerating found strings
perl -M5.010 -wpi.bak -e'our $article; s/&lt;text id="\K[0-9]+/++$article/ge' hugetextfile
