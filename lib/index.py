import lib.download as Download
import lib.upload as Upload


def upload(filePath, bucketName, s3Key, cseKeyArn):
  if cseKeyArn:
    return Upload.uploadEncrypted(filePath, bucketName, s3Key, cseKeyArn)

  return Upload.upload(filePath, bucketName, s3Key)

def download(filePath, bucketName, s3Key, cseKeyArn):
  if cseKeyArn :
    return Download.downloadEncrypted(filePath, bucketName, s3Key, cseKeyArn)
  
  return Download.download(filePath, bucketName, s3Key)

