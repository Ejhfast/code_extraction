# How to improve efficiency in this numpy iterating?
im2 = np.kron(im, np.ones((4,4)))
dm2 = np.tile(dithering_matrix,(512,512))
out2 = ((im2 / (256 / split_num)) &gt; dm2) * 255
