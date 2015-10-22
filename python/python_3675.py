# One last step! (python tuning)
'\n'.join(('\t'.join([field.strip().center(20) for
    field in [str(tup).center(20) for
        tup in rowTuple]])) for rowTuple in listOfRows)
