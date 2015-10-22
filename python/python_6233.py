# Python argparse: Make at least one argument required
if not (args.process or args.upload):
    parser.error('No action requested, add -process or -upload')
