import json

import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    try:
        table = dynamodb.Table('vehicleModel')
                   
        response = table.put_item(
            Item={
                    'model_id': 'M1002',
                    'model_name': 'Audi',
                    'model_type': 'Car'
                    }
        )
    
        return {
            'statusCode': 200,
            'message':'Success!'}
    except:
        return {
            'statusCode': 400,
            'body': 'Error, bad request!'}
