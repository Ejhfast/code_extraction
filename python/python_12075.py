# python - compare two directories recursively and flag equivalent structure
set((remove_version(filepath) for filepath in iter_file(dic1))) == set((remove_version(filepath) for filepath in iter_file(dic2)))
