# Can I get a list of users assigned to a project?
for membership in redmine.project.get('my_project').memberships:
    print membership.user_id
