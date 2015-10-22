# how to write std.error to file but std.out to console in python?
import sys
sys.stderr = open("/tmp/errors.txt", "w")
