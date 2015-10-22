# What is the Python syntax for adding the reduce part of a map/reduce pair in the ViewDefinition method of couchdb?
awk commands within python script
&gt;&gt;&gt; x = '''tail -n+2 ./*/*.tsv|cat|awk 'BEGIN{FS="\t"};{split($10,arr,"-")}{print arr[1]}'|sort|uniq -c'''
&gt;&gt;&gt; x
'tail -n+2 ./*/*.tsv|cat|awk \'BEGIN{FS="\t"};{split($10,arr,"-")}{print arr[1]}\'|sort|uniq -c'
