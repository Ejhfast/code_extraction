# Grouping django objects using QuerySet API by shared text tags using two models with ForeignKey relationship
Document.objects.filter(tagdb__tag_text__in=doc.tags_as_csv.split(' , ')).distinct()
