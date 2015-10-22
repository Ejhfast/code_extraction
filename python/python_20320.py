# How can I replace the first few bytes of a files with random data?
dd if=/dev/urandom of=myrandom bs=100 count=10 conv=notrunc
