# Fourier Series from Discrete Fourier Transform
y = ([(dft[nn].real)*np.cos(np.pi*x*nn) + (dft[nn].imag)*np.cos(np.pi*x*nn) for nn in range(0,n)])
