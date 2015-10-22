# Pricing a Floating Bond in quantlib using Python
cfs = floating_bond.cashflows()
coupons = [ as_coupon(c) for c in cfs[:-1] ] # the last one is the redemption
print [ (c.rate(), c.accrualPeriod()) for c in coupons ]
