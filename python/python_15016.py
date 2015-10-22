# Starting a stopped EC2 instance with Boto
instance = conn.get_all_instances(instance_ids=['instance_id'])
print instance[0].instances[0].start()
