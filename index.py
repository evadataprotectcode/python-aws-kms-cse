'use strict'

import os
import os.path as Path
import argparse
import lib.index as App


# internals.defintion = {
#   h: {
#     description: 'Show help',
#     alias: 'help',
#     type: 'boolean'
#   },
#   u: {
#     description: 'Upload a file',
#     alias: 'upload',
#     type: 'boolean',
#   },
#   d: {
#     description: 'Download a file',
#     alias: 'download',
#     type: 'boolean',
#   },
#   f: {
#     description: 'File to upload/download',
#     alias: 'file',
#     type: 'string',
#     require: True
#   },
#   b: {
#     description: 'S3 bucket name to upload/download',
#     alias: 's3Bucket',
#     type: 'string',
#     require: True
#   },
#   k: {
#     description: 'KMS key arn to use to encrypt the file',
#     alias: 'kmsArn',
#     type: 'string',
#   }
# }

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

  # if args instanceof Error:
  #   return console.error(args.message)


  if args.upload and args.download:
    return print('Please choose either upload or download, not both')


  file = args.file
  s3Bucket = args.s3Bucket
  kmsArn = args.kmsArn

  if args.upload:
    return upload(file, s3Bucket, kmsArn)


  if args.download:
    return download(file, s3Bucket, kmsArn)


  print('You must specify either --upload or --download')
  print(parser.print_help())
  # return print(Bossy.usage(internals.definition))


def upload(file, s3Bucket, kmsArn):
  dirname = os.getcwd()
  filePath = Path.join(dirname, file)
  s3Key = Path.basename(file)

  return App.upload(filePath, s3Bucket, s3Key, kmsArn)


def download(file, s3Bucket, kmsArn):
  dirname = os.getcwd()
  filePath = Path.join(dirname, file)
  print('File will be available here: ', filePath)

  return App.download(filePath, s3Bucket, file, kmsArn)


run()