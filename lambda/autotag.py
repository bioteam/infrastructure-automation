import json
import boto3
ec2 = boto3.client('ec2')


# The Lambda handler is the function that gets invoked by Lambda
# whenever the predetermined event arrives. It is passed information
# about the event, as well as has access to information about the
# execution context (which is not used in this function).

def lambda_handler(event, context):
    # Any output printed from Lambda gets stored in CloudWatch Logs
    # and can be seen through the Lambda or CloudWatch Logs consoles.
    # We print out the event (in JSON format) for troubleshooting.
    print(json.dumps(event))

    # The event coming from CloudWatch has many details in it,
    # including information about the user identity. The userName
    # property is only set when the event comes from an IAM user;
    # otherwise, the "username" is set to the principalId which is
    # always set and contains information about assumed roles or
    # federated users.
    principal_type = event['detail']['userIdentity']['type']
    if principal_type == 'IAMUser':
        username = event['detail']['userIdentity']['userName']
    else:
        username = event['detail']['userIdentity']['principalId']

    # Also contained within the event is the request and response data
    # surrounding the API call itself. Since this is triggered by a
    # RunInstances call, the response data contains a list of instance
    # IDs created by EC2. We extract those IDs using a list
    # comprehension.
    response = event['detail']['responseElements']
    ids = [i['instanceId'] for i in response['instancesSet']['items']]

    # Finally, with the list of IDs and the username determined, we
    # make an API call to EC2 using the boto3 library to create the
    # Owner tag on the instances.
    ec2.create_tags(Resources=ids, Tags=[{"Key": "Owner", "Value": username}])
