# Asyncio event loop per python process (aioprocessing, multiple event loops)
policy = asyncio.get_event_loop_policy()
policy.set_event_loop(policy.new_event_loop())
loop = asyncio.get_event_loop()
