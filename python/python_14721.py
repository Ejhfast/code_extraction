# PyTables Column to normal python list
mylist = h5file.root.mygroup.mytable.cols.mycolumn[:]
