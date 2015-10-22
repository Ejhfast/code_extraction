# Cut a large text file in small files
lines = open('myfile.txt').readlines()
for i in range(0, 1000000, 15000):
   open('{0}_{1}.txt'.format(i+1, i+15000), 'w').writelines(lines[i:i+15000])
