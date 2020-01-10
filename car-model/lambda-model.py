# ---------------------------------------
# Service for GET, POST car model details
# ---------------------------------------

import json
import ast
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    method = ''
    method = event['httpMethod']
    table = dynamodb.Table('model')

    if method == 'GET':
        query_string_params = event['queryStringParameters']
        data = table.scan()
        data = data['Items']

        if query_string_params == None:
            try:

                response = {
                    'statusCode': 200,
                    'body': json.dumps(data)
                }

                return response

            except:
                return {
                    'statusCode': 400,
                    'body': 'Error, bad request!'

                }
        else:
            try:
                for key, value in query_string_params.items():
                    if key == 'id':
                        id = value

                        response = table.get_item(
                            Key={
                                'model_id': id,
                            }
                        )

                        item = response['Item']
                        return {
                            'statusCode': 200,
                            'body': json.dumps(item)
                        }
                    if key != 'id' and key:
                        name = value
                        result_list = [d for d in data if d[key] == name]

                        return {
                            'statusCode': 200,
                            'body': json.dumps(result_list)
                        }
            except:
                return {
                    'statusCode': 400,
                    'body': 'Error, bad request!'
                }

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
