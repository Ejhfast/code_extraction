# Providing arguments to transactions in Datastore Plus (NDB)
yield context.transaction(lambda: increment_counter(acc.key(), 5))
