import json
import ast
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']
    table = dynamodb.Table('vehicleModel')

    if method == 'GET':
        return {
            'body': json.dumps(event)
        }
        # get_models(table)

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

def get_models(table):

    try:

        data = table.scan()

        response = {
            'statusCode': 200,
            'body': json.dumps(data['Items'])
        }

        return response

    except:
        return {
            'statusCode': 400,
            'body': 'Error, bad request!'
            
        }

def get_models(table, model_id):

    try:

        data = table.scan()

        response = {
            'statusCode': 200,
            'body': json.dumps(data['Items'])
        }

        return response

    except:
        return {
            'statusCode': 400,
            'body': 'Error, bad request!'
            
        }