# Numpy generate array from csv - doesnt work with only 1 value in csv
terms = [x for x in open(file_path,'r').read().replace('\n',',').split(',') if len(x)&gt;0]
