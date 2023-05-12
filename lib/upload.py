import lib.aws.s3 as s3
import lib.aws.cse as cse

def uploadEncrypted(file_path, bucket_name, s3_key, cse_key_arn):
  encrypted_text = cse.encrypt(file_path, cse_key_arn)
  return s3.upload(bucket_name, s3_key, encrypted_text)

def upload(file_path, bucket_name, s3_key):
  return s3.upload(bucket_name, s3_key, open(file_path, 'rb'))