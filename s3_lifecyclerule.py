import boto3

client = boto3.client('s3')
session = boto3.Session(profile_name='default', region_name='us-east-1')
s3 = session.resource('s3')
bucket_lifecycle_configuration = s3.BucketLifecycleConfiguration('venkatsampletest')

try:
        bucket_lifecycle_configuration.put(
            LifecycleConfiguration={
                'Rules': [
                    {
                        'Expiration': {
                            'Days': 10
                        },
                        'ID': 'life cycle config for log folder',
                        'Filter': {
                            'Prefix': 'python/',
                        },
                        'Status': 'Enabled',
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': 12
                        },
                        'AbortIncompleteMultipartUpload': {
                            'DaysAfterInitiation': 12
                        }
                    },
                ]
            }
        )
except Exception as e:
        print (e.message)
        exit(1)