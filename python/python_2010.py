# Extracting columns from text file using Perl one-liner: similar to Unix cut
perl -ane "print qq(@F[0..2]\n)" file.txt
