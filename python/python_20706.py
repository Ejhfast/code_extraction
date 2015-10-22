# Django celery chain
som = chain (task_async_get_me_friends.s(userId),parse_friends.s())
