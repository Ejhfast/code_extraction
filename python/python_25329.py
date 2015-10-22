# Which flag for run_flow() will simulate the now deprecated run()
flags = tools.argparser.parse_args(args=[])
credentials = tools.run_flow(flow, storage, flags)
