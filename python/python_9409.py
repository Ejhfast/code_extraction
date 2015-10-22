# Django Admin: Order by value on related Foreign Key
def queryset(self, request):
        qs = super(ContentAdmin, self).queryset(request)
        return qs.filter(score__name='Twitter').order_by('-score__score')
