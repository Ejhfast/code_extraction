# python script for downloading all Ctrl+Alt+Del webcomics?
$ for filename in $(seq 20020101 20090726); do wget http://www.ctrlaltdel-online.com/comics/"$filename".jpg; done
