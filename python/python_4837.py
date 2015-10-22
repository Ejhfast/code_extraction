# Efficient math operations on parts of "sparse" numpy arrays
height_r_t = np.ma.masked_where(repelling_force_prefactor == 0, height_r_t)
repelling_forces = np.ma.exp(-(height_r_t/potential_steepness))
