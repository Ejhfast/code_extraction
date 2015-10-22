# replace None with Null, in place
result = [TestCase.productUnderTest,TestCase.versionUnderTest,TestCase.name,TestCase.results,TestCase.lastTestEnd,TestCase.parent,TestCase.level]
result = map(lambda x:x==None and 'Null' or str(x), result)
ME.csvoutput.write(",".join(result)+'\n')
