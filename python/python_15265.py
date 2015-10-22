# How to detect if a commit has been done on a remote SVN repo
url="svn://xx.xx.xx.xx/proj_name/"
newest="$( svn log -r HEAD -q "$url" | sed -ne '/^r[0-9]*\).*$/s//\1/p' )"
