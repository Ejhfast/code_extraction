# Python logging dictionary config
import yaml
logging.config.dictConfig(yaml.load(open('logging.config', 'r')))
