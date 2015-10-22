# Find files with multiline strings matched
perl -lne '/^115,55/ ... /^\d/ and /^,123:400/ or next;print $ARGV;close ARGV' *udr
