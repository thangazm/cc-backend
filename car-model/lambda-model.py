import json

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']

    if method == 'GET':
        table = dynamodb.Table('vehicleModel')
        data = table.scan()

        response = {
        'statusCode': 200,
        'body': json.dumps(data['Items'])
        }
        return response
        
    if method == 'POST':

        response = table.put_item(
            Item=event['body']
        )
        
        return response
