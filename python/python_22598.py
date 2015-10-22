# how to execute LIKE query in sqlalchemy?
select([self.audit_trail_table]).where(self.audit_trail_table.c.first_name.like('%' + filter_query + '%') or self.audit_trail_table.c.last_name.like('%abc%'))
