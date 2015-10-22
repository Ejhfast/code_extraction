# sort two joined querysets - django
sorted_qs = sorted(chain(fqs, sqs), key=lambda obj: obj.added)
