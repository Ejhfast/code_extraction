# Use ldap3 to query all active directory groups a user belongs to
ldap3.Reader(c, person, '(&amp;(member=CN=myuser_in_full_name,OU=xxx,OU=xxxxxx,DC=mydomain,DC=com)(objectClass=group))', 'dc=mydomain,dc=com').search()
