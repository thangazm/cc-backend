# ---------------------------------------
# Service for GET, POST car price details
# ---------------------------------------

import json
import ast
import boto3
import uuid

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']
    table = dynamodb.Table('price')

    # if method == 'GET':
    if method == 'POST':
        try:
            post_data = event['body']
            jsondata = ast.literal_eval(post_data)
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