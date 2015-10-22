# Peewee: how to select multiple rows where id matches the list?
Job.select().join(User).where(Job.id &lt;&lt; list_of_ids.split(','))
