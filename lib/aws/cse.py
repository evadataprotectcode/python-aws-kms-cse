import boto3


def encrypt(file_name, key_arn):
  client = boto3.client('kms')

  file_in_bytes = open(file_name, 'rb')
  encryption = client.encrypt(
    KeyId=key_arn,
    Plaintext=file_in_bytes.read()
  )

  return encryption['CiphertextBlob']


def decrypt(cipher_text_blob, key_arn):
  client = boto3.client('kms')

  decryption = client.decrypt(
    KeyId=key_arn,
    CiphertextBlob=cipher_text_blob
  )

  return decryption['Plaintext']

