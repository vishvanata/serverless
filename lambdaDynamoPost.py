import boto3
import json

print('Loading function')
dynamodb = boto3.resource('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    table = dynamodb.Table('muvirtTable')
    payload = json.loads(event['body'])
    response = table.put_item(
        Item=payload
        )
        
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
