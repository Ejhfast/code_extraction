# Is it possible to calculate the value of a field from another field in the same form in OpenERP?
def on_change_interest_fields(self, cr, uid, ids, amountPay, interestType, context):
    interest = amountPay * 0.5
    return {'value': {'interest': interest,},}
