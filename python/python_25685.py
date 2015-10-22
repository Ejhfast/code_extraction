# Python extracting a subset from tuple that is sql result
Students.objects.filter(studentid__in=[p[0] for p in ids[:10]])
