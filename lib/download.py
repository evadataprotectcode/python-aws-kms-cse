import lib.aws.s3 as s3
import lib.aws.cse as cse

def downloadEncrypted(file_path, bucket_name, s3_key, cse_key_arn):
  body = s3.download(s3_key, bucket_name)
  content = body.read()
  decrypted_content = cse.decrypt(content, cse_key_arn)
  f = open(file_path, 'wb')
  return f.write(decrypted_content)

def download(file_path, bucket_name, s3_key):
  return s3.download_file(s3_key, bucket_name, file_path)
  