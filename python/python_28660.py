# Django: How to manage groups and permission without using default admin
filter_show_permissions = ["perm_a", "perm_b", ...]
filtered_permissions = [perm for perm in user.user_permissions
                        if perm in filter_show_permissions]
