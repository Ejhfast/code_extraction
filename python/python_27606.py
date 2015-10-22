# Combination of chdir=1 and num_jobs>1 in SCons
env.Command(b,a,"cd ${SOURCE.dir}; do whatever -o ${TARGET.file} -i ${SOURCE.file}").
