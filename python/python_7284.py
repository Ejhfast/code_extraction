# Python function to sum digits
def getSumOfLastDigits(numList):
  return sum(x % 10 for x in numList)
