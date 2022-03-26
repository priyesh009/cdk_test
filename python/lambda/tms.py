import json
import boto3
from boto3.dynamodb.conditions import Key
import os
dynamodb = boto3.resource('dynamodb')
GET_RAW_PATH = "/gettask"
CREATE_RAW_PATH = "/createtask"
TABLE_NAME = os.environ.get('tms_table')


def lambda_handler(event, context):
    print(event) 
    table = dynamodb.Table(TABLE_NAME)
    if event['rawPath'] == GET_RAW_PATH:
        url = event['queryStringParameters']['URL']
        print(url)
        lst =url.split('/')
        if len(lst) <2:
            raise Exception
        PK = lst[0]
        SK = '/'.join(lst[1:])
        
        print("args " ,  PK, SK)
        body = gettask(table,PK,SK)
        statusCode=200
    elif event['rawPath'] == CREATE_RAW_PATH:
        payload = event['body']
        body = createtask(table,payload)
        statusCode=200
    else:
        statusCode=400
        
    return {
        'statusCode': statusCode,
        'body': json.dumps(body),
        'headers' : {
            "Content-Type" : "application/"
        }
    }


def gettask(table,pkid,skid):
    "To retrive the task from DynamoDB"
    try:

        response = table.query(
        KeyConditionExpression=Key('PK').eq(pkid) & Key('SK').begins_with(skid)
        #FilterExpression = Key('SK').begins_with(skid)
)
        return response['Items']        
    except KeyError:
        return "error occured ID not present"

    
    
def createtask(table,payload):
    "To add the task info into the DynamoDB"
    try:
        res=json.loads(payload)
        resp = table.put_item(
        Item=dict(res) 
        )
        body = 'Hello Lambda from create task'
        return body
    except:
        return "error occured enter both PK and SK"    
    