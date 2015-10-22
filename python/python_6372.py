# Including Duplicate Tables using Django's ORM Extra()
qs = Triple.objects.filter(subject="bob", predicate="knows").extra(select={'known': "t1.subject"}, tables=['"triple_triple" AS "t1"'], where=['triple_triple.object=t1.subject AND t1.predicate="has-a" AND t1.object="house"'])
