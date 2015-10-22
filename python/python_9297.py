# Mongo and regexp
namesWithE = family.find({name : {$regex : 'E.*'}})
