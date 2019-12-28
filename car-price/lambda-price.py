# ---------------------------------------
# Service for GET, POST car price details
# ---------------------------------------

import json
import ast
import boto3
import uuid
from boto3 import client as boto3_client

lambda_client = boto3_client('lambda', region_name="us-east-1")

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
    if method == 'GET':
        data = table.scan()

         response = lambda_client.invoke(
            FunctionName="cc-lambda-cf-stack-carLambdaPrice-J8KNKVM1XEU2",
            InvocationType='RequestResponse',
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
        # try:
            
        #     return {
        #         'statusCode': 200,
        #         'body': json.dumps(value)
        #     }
        # except:
        #     return {
        #         'statusCode': 400,
        #         'body': 'Error, bad request!'
        #     }
        