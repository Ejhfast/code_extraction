# save output as text file in networkx
with open('some_file.txt', 'w') as f:
   for k in sorted(your_dic):
      f.write("{}:{}\n".format(k, your_dic[k]))
