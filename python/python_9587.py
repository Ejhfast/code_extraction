# Find and replace in a specific column
perl -pale '$F[3]=~s/[.,]/$F[2]/g;$_=join" ",@F' file
