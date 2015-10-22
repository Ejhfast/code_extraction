# Querying in redis
user_to_resource:i = user:j                   # key -&gt; value forward map
 resources =&gt; (resource:i, created_timestamp)  # sorted set
 count_resource:i = quantity                   # key -&gt; value quantity map
