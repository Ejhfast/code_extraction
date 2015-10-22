# Python (django) how to deal with money calculations accurately
def r2(v):
    return Decimal(v).quantize(Decimal('0.00'))
