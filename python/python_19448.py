# Querying association table object directly
session.query(task_user).join(Task).join(User).filter(Task.group_id == group_id)
