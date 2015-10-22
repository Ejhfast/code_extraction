# Python - mask multidimensionnal
mask3 = mask2 * np.ones(3)[:, None, None].
masked_output = np.ma.array(frametemperature_reshape, mask=mask3)
