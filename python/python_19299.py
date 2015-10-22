# Filtering of structured array via bit-wise operation (bitmask) on column data
mask = (data['event_type'] &amp; event_type).astype(bool)
