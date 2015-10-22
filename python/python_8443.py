# Overriding admin views - Django
class SuperUserAdminSite( AdminSite ):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff and request.user. is_superuser
