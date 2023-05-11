import lib.aws.s3 as s3
import lib.aws.cse as cse

def downloadEncrypted(filePath, bucketName, s3Key, cseKeyArn):
  body = s3.download(s3Key, bucketName)
  content = body.read()
  decryptedContent = cse.decrypt(content, cseKeyArn)
  f = open(filePath, 'wb')
  return f.write(decryptedContent)

def download(filePath, bucketName, s3Key):
  return s3.download_file(s3Key, bucketName, filePath)
  