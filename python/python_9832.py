# convert numpy array to cython pointer
cdef np.ndarray[np.uint32_t, ndim=3, mode = 'c'] np_buff = np.ascontiguousarray(im, dtype = np.uint32)
cdef unsigned int* im_buff = &lt;unsigned int*&gt; np_buff.data
