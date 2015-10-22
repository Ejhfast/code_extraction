# How to preserve Image Quality when rotating with PIL
rotated_small = photo_small.rotate(angle, resample=Image.BICUBIC, expand=True)
