# SQLAlchemy: How do I find second degree relationships in the database?
user_abilities = []
for role in current_user.roles:
    user_abilities += [role.ability for ability in role.abilities]
