# python script has an output, but in a shell for loop it doesn't output
for i in *;do current_dir=$PWD; cd $PWD/$i;python ../importpymol2.py 65_*.pdb BTB_old.pdb;cd $current_dir; done
