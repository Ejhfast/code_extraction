# Boto: Dynamically get aws_access_key_id and aws_secret_access_key in Python code from config?
import boto
access_key = boto.config.get_value('Credentials', 'aws_access_key_id')
secret_key = boto.config.get_value('Credentials', 'aws_secret_access_key')
