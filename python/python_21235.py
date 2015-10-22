# How to submit a query in pyES?
def state_query(doc):
    return TermQuery(field="STATE_ALPHA", value=doc["state"].lower())
