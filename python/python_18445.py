# Linear decrease of a sound in Jython -- variable trouble
for index, sample in enumerate(getSamples(sound)):
    setSampleValue(sample, int((((min-max)/length) * index) + max))
