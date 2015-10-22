# Is a mutex really necessary in this piece of code?
def increment(self, seconds):
    with self._mutex:
        self._countdownInSec += seconds
