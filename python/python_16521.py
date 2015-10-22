# How do you connect to AWS Elastic Transcoder?
import boto.elastictranscoder
transcode = boto.elastictranscoder.connect_to_region('us-west-2')
transcode.create_job(...)
