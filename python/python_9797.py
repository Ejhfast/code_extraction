# Python default / optional Variables
class ScoredList():
    def __init__(self, dct=None):
        self.dct = dct if dct is not None else {}
