import logging
import boto3
from botocore.exceptions import ClientError
import aws_encryption_sdk
import os


def download_file(object_name, bucket, file_name):
  # Upload the file
  s3 = boto3.client('s3')

  try:
    return s3.download_file(bucket, object_name, file_name)

  except ClientError as e:
      logging.error(e)
      return False
  return True

def download(object_name, bucket):
  # Upload the file
  s3 = boto3.client('s3')

  try:
      response = s3.get_object(
        Bucket=bucket,
        Key=object_name)

      return response['Body']
  except ClientError as e:
      logging.error(e)
      return False
  return True

def upload(bucket, object_name, body):
  # Upload the file
  s3 = boto3.client('s3')

  try:
    return s3.put_object(
      Bucket=bucket,
      Key=object_name,
      Body=body)
  except ClientError as e:
      logging.error(e)
      return False
  return True