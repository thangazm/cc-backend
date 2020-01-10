# cc-backend

## Build and Deployment

Add Functions to path and add them to samsourceTemp.yml file

i.e.:

```
carLambdaModel:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: lambda-model.lambda_handler
      Runtime: python3.6
      CodeUri: ./car-model
      Description: 'Lambda function for to GET POST car model'
      MemorySize: 512
      Timeout: 30
      Role: 'arn:aws:iam::015320530739:role/cc-lambda-pipeline'
      Events:
        searchModelAPI:
          Type: Api
          Properties:
            Path: /model
            Method: GET
        postModelAPI:
          Type: Api
          Properties:
            Path: /model
            Method: POST
```

Add DynamoDB tables to samsourceTemp.yml file

i.e.:

```
  model:
    Type: 'AWS::DynamoDB::Table'
    Properties:
      TableName: model
      AttributeDefinitions:
        - AttributeName: model_id
          AttributeType: S
      KeySchema:
        - AttributeName: model_id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
```

All the functions and tables will be build and executed via the pipeline and you can check them from the aws account.

Check the cloud watch for logs and debug your function