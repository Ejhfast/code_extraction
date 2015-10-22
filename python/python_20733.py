# Python xlwt can't parse "complex" formula, reference to another worksheet
xlwt.Formula("ROUND(SUM('%s'!$G$%d:$G$%d);0)" % (u"Hungarian word", intval[0], intval[1])))
