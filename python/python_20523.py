# Django - Restricting User Access to the Admin Site
class TeamModelAdmin(admin.ModelAdmin):
    def get_queryset(request):
         return Team.objects.filter(...)
