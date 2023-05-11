import lib.aws.s3 as s3
import lib.aws.cse as cse

def uploadEncrypted(filePath, bucketName, s3Key, cseKeyArn):
  encryptedText = cse.encrypt(filePath, cseKeyArn)
  return s3.upload(filePath, bucketName, s3Key, encryptedText)

def upload(filePath, bucketName, s3Key):
  return s3.upload(filePath, bucketName, s3Key, open(filePath, 'rb'))