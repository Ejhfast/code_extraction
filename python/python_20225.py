# pendant to inline formsets for many-to-many relations
RoleFormSet = inlineformset_factory(UserRole, User.role.though)
