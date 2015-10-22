# Stop execution of python script when parent Bash shell script is killed
trap "echo killing childs; pkill -P $$"  EXIT
