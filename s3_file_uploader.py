import boto3
import os

client = boto3.client('s3')

#path = "C:\Users\venkatesan.k\PycharmProjects\PythonAWS"
for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'venkatsampletest'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
