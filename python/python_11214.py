# Jinja Templates - Format a float as comma-separated currency
def format_currency(value):
    return "${:,.2f}".format(value)
