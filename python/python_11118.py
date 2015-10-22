# argparse: setting optional argument with value of mandatory argument
ns = parser.parse_args()
ns.extra_file = ns.extra_file if ns.extra_file else ns.filename
