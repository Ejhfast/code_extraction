# File encoding from English text to UTF-8
iconv -f `uchardet a_strange_file.txt` -t UTF-8 -o the_output_file.txt a_strange_file.txt
