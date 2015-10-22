# How do I find the exact CLI command given to the python?
import pipes # or shlex if python3
print sys.argv[0], ' '.join( [pipes.quote(s) for s in sys.argv[1:]] )
