import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('reddit_parse')

def lambda_handler(event, context):
    # TODO implement ############################## USE PARAMS TO SPECIFY STOCK
    response = table.get_item(
        Key={
            'stock': event["stock"]
        }
    )
    return {
        'statusCode': 200,
        'body': response
    }
