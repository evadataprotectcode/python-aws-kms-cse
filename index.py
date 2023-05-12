'use strict'

import os
import os.path as Path
import argparse
import lib.index as App


def run():
  parser = argparse.ArgumentParser()

  parser.add_argument(
    '-u', 
    '--upload', 
    action='store_true',
    help='Upload a file')

  parser.add_argument(
    '-d', 
    '--download', 
    action='store_true',
    help='Download a file')

  parser.add_argument(
    '-f', 
    '--file', 
    action='store',
    help='File to upload/download',
    required=True)

  parser.add_argument(
    '-b', 
    '--s3Bucket', 
    action='store',
    help='S3 bucket name to upload/download',
    required=True)
  
  parser.add_argument(
    '-k', 
    '--kmsArn',
    action='store',
    help='KMS key arn to use to encrypt the file')


  args = parser.parse_args();


  if args.upload and args.download:
    return print('Please choose either upload or download, not both')


  file_name = args.file
  s3_bucket = args.s3Bucket
  kms_arn = args.kmsArn

  if args.upload:
    return upload(file_name, s3_bucket, kms_arn)


  if args.download:
    return download(file_name, s3_bucket, kms_arn)


  print('You must specify either --upload or --download')
  parser.print_help()


def upload(file_name, s3_bucket, kms_arn):
  dirname = os.getcwd()
  filePath = Path.join(dirname, file)
  s3Key = Path.basename(file)

  return App.upload(file_path, s3_bucket, s3_key, kms_arn)


def download(file_name, s3_bucket, kms_arn):
  dirname = os.getcwd()
  file_path = Path.join(dirname, file)
  print('File will be available here: ', file_path)

  return App.download(file_path, s3_bucket, file_name, kms_arn)


run()