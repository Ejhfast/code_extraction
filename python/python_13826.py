# Overriding default argparse -h behaviour
parser = argparse.ArgumentParser('Cool', add_help=False)
parser.add_argument('-h', '--hi', action='store_true', dest='hi')
