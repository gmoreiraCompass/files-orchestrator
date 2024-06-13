import boto3

class Config:
  def __init__(self, aws_access_key, aws_access_secret):
    self.aws_access_key = aws_access_key
    self.aws_access_secret = aws_access_secret

  @staticmethod
  def session():
    return boto3.Session(
      aws_access_key_id = self.aws_access_key,
      aws_secret_access_key = self.aws_access_secret
    )