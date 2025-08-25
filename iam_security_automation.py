import boto3
from datetime import datetime, timedelta

iam = boto3.client('iam')
users = iam.list_users()['Users']

for user in users:
    keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
    for key in keys:
        if key['Status'] == 'Active' and key['CreateDate'] < datetime.now() - timedelta(days=90):
            print(f"Rotating key {key['AccessKeyId']} for user {user['UserName']}")
            
