# Buildbot force build via python
buildbot sendchange --master {MASTERHOST}:{PORT} --auth {USER}:{PASS}
    --who {USER} {FILENAMES..}
