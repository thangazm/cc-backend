# ---------------------------------------
# Service for GET, POST car price details
# ---------------------------------------

import json
import ast
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']

    # if method == 'GET':
    if method == 'POST':
        try:
            jsondata = ast.literal_eval(event['body'])
            value = table.put_item(
                Item=jsondata
            )
            return {
                'statusCode': 200,
                'body': json.dumps(value)
            }
        except:
            return {
                'statusCode': 400,
                'body': 'Error, bad request!'
            }