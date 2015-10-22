# Pass expression as named argument name
def time_delta(age):
    now = datetime.fromtimestamp(int(time.time()))
    return now - relativedelta(**{age.time_unit: int(age.value)})
