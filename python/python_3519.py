# python function list chained executing?
def execu(lst, seq, raw_para):
  return reduce(lambda x, y: y(x), reversed(operator.itemgetter(*seq)(lst)), raw_para)
