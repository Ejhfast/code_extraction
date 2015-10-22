# Swap lines in a script by iteration over lines
perl -ne 'push @r, $_; print(@r[2,1,0,3]), @r=() if @r==4 or eof' file
