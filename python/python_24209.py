# Numpy array Regex sub
print(np.array(list(map(lambda v: re.sub(r'^A','XA', v) ,arr))))
% outputs: ['XAB' 'XAC' 'XAB' 'XAC' 'XAD']
