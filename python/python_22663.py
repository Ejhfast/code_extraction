# How do I exclude directories when using os.walk()? Other methods haven't worked
exclude = set(["faces","animations"])
for root,subdirs,files in os.walk(topDir):
    subdirs[:] = [d for d in set(subdirs)-exclude]
