# how to output multiple files from a set of different input files for a python script in bash
for i in X Y Z; do
    python myscript.py /folder[1-5]/chr$i.vcf.gz &gt; /myNewFolderForOutputs/chr${i}output.txt
done
