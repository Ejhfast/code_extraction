# python test result reporting
for x in results.successes + results.failures + results.errors:
    print x
    #print x.get_description(), x.outcome
