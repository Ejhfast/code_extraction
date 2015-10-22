# Django admin performance issue
class MyModelAdmin(admin.ModelAdmin):
    list_select_related = True
    # ....
