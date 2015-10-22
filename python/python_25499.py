# Popen.communicate() returns (None, None) even if script print results
to get anything other than None in the result tuple, you need to give stdout=PIPE and/or stderr=PIPE
