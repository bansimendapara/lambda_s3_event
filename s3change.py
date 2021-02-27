import json
import boto3
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    table = dynamodb.Table('s3change')
    
    s3Event = event['Records'][0]
    print(s3Event)
    
    requestID = context.aws_request_id
    
    dateTime = s3Event['eventTime']
    eventDateTimePST = datetime.strptime(dateTime, "%Y-%m-%dT%H:%M:%S.%f%z") - timedelta(hours=8)
    eventDate = eventDateTimePST.strftime('%m-%d-%Y')
    eventTime = eventDateTimePST.strftime('%I:%M:%S %p')
    
    eventName = s3Event['eventName']
    
    object = s3Event['s3']['object']['key'].replace('+',' ')
    
    if eventName[:13]=='ObjectRemoved':
        size = 'N/A'
    else:
        size = str(s3Event['s3']['object']['size'])
    
    table.put_item(
        Item={
            'RequestID': requestID,
            'Date': eventDate,
            'Time': eventTime,
            'EventType': eventName,
            'Object': object,
            'Size': size
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
