# Can one make Python constructors more concise?
class Country:
    def __init__(self, population, literacy, firms, area, populationDensity):
        (self.population, self.literacy, self.firms, self.area, self.populationDensity) = (population, literacy, firms, area, populationDensity)
