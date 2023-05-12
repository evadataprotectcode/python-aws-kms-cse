import lib.download as Download
import lib.upload as Upload


def upload(file_path, bucket_name, s3_key, cse_key_arn):
  if cse_key_arn:
    return Upload.uploadEncrypted(file_path, bucket_name, s3_key, cse_key_arn)

  return Upload.upload(file_path, bucket_name, s3_key)

def download(file_path, bucket_name, s3_key, cse_key_arn):
  if cse_key_arn :
    return Download.downloadEncrypted(file_path, bucket_name, s3_key, cse_key_arn)
  
  return Download.download(file_path, bucket_name, s3_key)

