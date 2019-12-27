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
        # return {
        #     'body': json.dumps(event)
        # }
        # get_models(table)
        query_string_params = event['queryStringParameters']
        if query_string_params == None:
            get_models(table)
        else:
            for param, value in query_string_params.keys():
                if param == 'id':
                    id = value
                    get_models_by_id(table, id)
                if param == 'name':
                    name = values
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

def get_models_by_id(table, model_id):

    try:

        response = table.get_item(
            Key={
                'model_id': model_id,
            }
        )

        # response = {
        #     'statusCode': 200,
        #     'body': json.dumps(data['Items'])
        # }

        # return response

    except ClientError as e:
        return e.response['Error']['Message']
    else:
        item = response['Item']
        return json.dumps(item, indent=4, cls=DecimalEncoder)