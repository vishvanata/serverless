import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = client.query(
        TableName= 'muvirtTable',
        KeyConditionExpression='SLNO = :mvalue',
        ExpressionAttributeValues={
            ':mvalue' : {'S':event['params']['querystring']['SLNO']}
        }
    )
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": response
    }
