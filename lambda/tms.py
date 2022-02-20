import json
import boto3

dynamodb = boto3.resource('dynamodb')
GET_RAW_PATH = "/gettask"
CREATE_RAW_PATH = "/createtask"
TABLE_NAME = 'CdkTestStack-tmsTable5AC380E7-FCG7COKMTHXV'


def lambda_handler(event, context):
    print(event) 
    table = dynamodb.Table(TABLE_NAME)
    if event['rawPath'] == GET_RAW_PATH:
        PKId = event['queryStringParameters']['PK']
        print("with param PK ID=" + PKId)
        body = gettask(table,PKId)
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


def gettask(table,id):
    "To retrive the task from DynamoDB"
    res = table.get_item(
        Key = {
            'PK':id
        }
        )
    body = 'Hello Lambda from get task' + str(res['Item'])
    return body
    
    
def createtask(table,payload):
    "To add the task info into the DynamoDB"
    res=json.loads(payload)
    resp = table.put_item(
    Item=dict(res) 
    )
    body = 'Hello Lambda from create task'
    return body
    
    
def access_pattern():
    "To add the task info into the DynamoDB"
    pass