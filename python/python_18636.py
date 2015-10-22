# What is a way of accessing arbitrary groups in hdf5 file using pytables?
row_str = 'h5f.root.{}'.format(user)
    where = eval(row_str)
    subjectGroup = h5f.createGroup(where, subjectName)
