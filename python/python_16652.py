# group element by two python list
res = [ "{}\t{}\n".format(x,y)
          for (x,y) in zip(datacolumn[0::2], datacolumn[1::2])]
