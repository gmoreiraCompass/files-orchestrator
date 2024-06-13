import sys
from aws_config import Config

bucket_name=sys.argv[1]
aws_key=sys.argv[2]
aws_access_key=sys.argv[3]
aws_access_secret=sys.argv[4]
local_path=sys.argv[5]

Config(aws_access_key,aws_access_secret)
clientS3 = Config.clientS3()