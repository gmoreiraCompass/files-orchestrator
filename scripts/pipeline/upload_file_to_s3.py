import sys
from aws_config import Config

def main():
  print(sys.argv)
  if (len(sys.argv) < 6):
    print('Error: Required 5 arguments.')
    # Checks for 6 because the script path is in position 0. So len is 6
    # for 5 arguments.
    sys.exit(1)
  
  bucket_name=sys.argv[1]
  aws_key=sys.argv[2]
  aws_access_key=sys.argv[3]
  aws_access_secret=sys.argv[4]
  local_path=sys.argv[5]

  Config(aws_access_key, aws_access_secret)
  clientS3 = Config.session().client('s3')

  response = client.upload_file(
    Filename=local_path,
    Bucket=bucket_name,
    Key=aws_key
  )
  print('Done uploading')

main()