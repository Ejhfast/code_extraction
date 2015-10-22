# python subclasses
class Quadratic(Polynomial):
    def __init__(self, quadratic, linear, constant):
        Polynomial.__init__(self, (2, quadratic), (1, linear), (0, constant))
