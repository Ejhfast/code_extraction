# Python 3: Optimizing summation over scipy arrays
H_bis = np.sum(M[1:2*n**2:2, :2*n**2] * M[:2*n**2:2, :2*n**2].conjugate(), axis=1)
H_bis = H_bis * H_bis.conjugate()
H_bis = -np.sum(H_bis)
