# Python-ldap not able to bind successfully
conn.protocol_version = ldap.VERSION3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s(user, pw)
