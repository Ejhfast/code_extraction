# What is the simplest way to round a floating point number up to the next integer in Python?
def calculateGallonsNeeded(fltWallArea,AREA_UNIT):
    fltGallonsNeeded = math.ceil(fltWallArea / AREA_UNIT)
    return fltGallonsNeeded
