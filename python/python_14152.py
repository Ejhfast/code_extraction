# Z3py: Array of specific integer type?
Byte = BitVecSort(8)
i8 = BitVec('i8', Byte)
A = Array('A', IntSort(), Byte)
