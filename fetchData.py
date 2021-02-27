import json
import boto3
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    table = dynamodb.Table('s3change')

    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    print(data)
    
    responseBody = json.dumps(data)
    
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return apiResponse