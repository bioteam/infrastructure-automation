import json
import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(json.dumps(event))
    principal_type = event['detail']['userIdentity']['type']
    if principal_type == 'IAMUser':
        username = event['detail']['userIdentity']['userName']
    else:
        username = event['detail']['userIdentity']['principalId']
    
    response = event['detail']['responseElements']
    ids = [i['instanceId'] for i in response['instancesSet']['items']]
    ec2.create_tags(Resources=ids, Tags=[{"Key": "Owner", "Value": username}])
