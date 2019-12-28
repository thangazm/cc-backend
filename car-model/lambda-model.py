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
        # return {
        #     'body': json.dumps(query_string_params)
        # }
        if query_string_params == None:
            # get_models(table)
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
        else:
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
                        'body': json.dumps(item)
                    }
                if key == 'name':
                    name = value
                    data = table.scan()
                    # print(data['Items'])
                    for model in data['Items']:
                        print(model)
                        for key, value in model.items():
                            if key == 'model_name' and value == name:
                                    # result =a {}
                              return {
                                  'body': json.dumps(model)
                              } 
                              
                    # response = table.get_item(
                    #     Key={
                    #         "model_name": name,
                    #     }
                    # )
                    
                    # item = response['Item']
                    # return {
                    #     'body': json.dumps(result)
                    # }
            # print(query_string_params['id'])
            # return {
            #         'statusCode': 200,
            #         'body': json.dumps(query_string_params['id'])
            #     }
            # if query_string_params['id'] not None:
            #     try:
                    
            #         response = table.get_item(
            #             Key={
            #                 'model_id': query_string_params['id'],
            #             }
            #         )
                    
            #         item = response['Item']
            #         return {
            #             'body': json.dumps(item)
            #         }
            #     except:
                    
            #         return {
            #             'statusCode': 400,
            #             'body': 'Error, bad request!'
                        
            #         }
                
            # if query_string_params['name'] not None:
            #     try:
                    
            #         response = table.get_item(
            #             Key={
            #                 'model_name': query_string_params['name'],
            #             }
            #         )
                    
            #         item = response['Item']
            #         return {
            #             'body': json.dumps(item)
            #         }
            #     except:
            #         return {
            #             'statusCode': 400,
            #             'body': 'Error, bad request!'
                        
            #         }
            # for param, value in query_string_params.keys():
                
                # if param == 'id':
                #     return {
                #         'body': json.dumps(value)
                #     }
                #     id = value
                    # get_models_by_id(table, id)
                    # try:
                    
                    # response = table.get_item(
                    #     Key={
                    #         'model_id': id,
                    #     }
                    # )
                    # item = response['Item']
                    # return json.dumps(item, indent=4, cls=DecimalEncoder)
                        # response = {
                        #     'statusCode': 200,
                        #     'body': json.dumps(data['Items'])
                        # }
                
                        # return response
                
                    # except ClientError as e:
                    #     return e.response['Error']['Message']
                    # else:
                    #     item = response['Item']
                    #     return json.dumps(item, indent=4, cls=DecimalEncoder)
                # if param == 'name':
                #     name = values
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