import boto3

class Config(aws_access_key, aws_access_secret):
  @staticmethod
  def session(aws_access_key, aws_access_secret):
    return boto3.Session(
      aws_access_key_id=aws_access_key,
      aws_secret_access_key=aws_access_secret
    )

  @staticmethod
  def clientS3():
    return Config.session.client('s3')