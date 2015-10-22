# Why does python keep buffering stdout even when flushing and using -u?
-u     Force stdin, stdout and stderr to be totally unbuffered.  On systems where it matters, also put stdin, stdout and stderr in binary mode.  Note that
          there  is  internal  buffering  in  xreadlines(),  readlines()  and file-object iterators ("for line in sys.stdin") which is not influenced by this
          option.  To work around this, you will want to use "sys.stdin.readline()" inside a "while 1:" loop.
