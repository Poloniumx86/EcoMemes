import boto3
import random
import os

# Replace with your AWS credentials and S3 details
aws_access_key_id = 'AKIA5AVSWOGCIMVZAYFZ'
aws_secret_access_key = 'AOsbt2F/BucEaG4+ZeoVRPiq5u8bf1EuhBrJuM+K'
region_name = 'eu-west-2'
bucket_name = 'hacksheffield-8'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# List objects in the S3 bucket
response = s3.list_objects(Bucket=bucket_name)

# Extract the keys (names) of all objects in the bucket
all_keys = [obj['Key'] for obj in response.get('Contents', [])]

# Randomly pick an item
def File_Name():
    return random.choice(all_keys)
