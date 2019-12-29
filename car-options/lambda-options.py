# ----------------------------------
# Service for GET, POST car options
# ----------------------------------

import json
import ast
import boto3
from boto3 import client as boto3_client
from collections import defaultdict
from operator import itemgetter
from decimal import Decimal

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
lambda_client = boto3_client('lambda', region_name="us-east-1")

def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']
    table = dynamodb.Table('options')

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
        try:
            data = table.scan()
            payload = {}
            payload['httpMethod'] = 'GET'
            payload['queryStringParameters'] = None

            # call lambda function to get all the models available
            response_model = lambda_client.invoke(
                FunctionName="cc-lambda-cf-stack-carLambdaModel-J61DSV3WJ0O6",
                InvocationType='RequestResponse',
                Payload= json.dumps(payload)
            )
            
            res_json = json.loads(response_model['Payload'].read().decode("utf-8"))
            models = json.loads(res_json['body']) # returns a list of all models
            options_list = data['Items']

            d = defaultdict(dict)
            for l in (model, options_list):
                for elem in l:
                    d[elem['model_id']].update(elem)

            combine_list = sorted(d.values(), key=itemgetter("model_id"))

            return {
                'statusCode': 200,
                'body': json.dumps(combine_list)
            }
        except:
            return {
                'statusCode': 400,
                'body': 'Error, bad request!'
            }