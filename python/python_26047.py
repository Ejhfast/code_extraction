# Django with python3, results of sql query in selectbox
def __str__(self):
    related = PR_ComponentsData.objects.filter(id=self.id).last()
    return "{} ({})".format (related.comp_text, self.comp_nr)
