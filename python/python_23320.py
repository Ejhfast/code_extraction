# Fastest method to do an FFT
fft = pyfftw.builders.fft2(a, overwrite_input=True, planner_effort='FFTW_ESTIMATE', threads=multiprocessing.cpu_count())
b = fft()
