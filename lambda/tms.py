import json

GET_RAW_PATH = "/gettask"
CREATE_RAW_PATH = "/createtask"

def lambda_handler(event, context):
    print(event)

    if event['rawPath'] == GET_RAW_PATH:
        body = gettask()
        statusCode=200
    elif event['rawPath'] == CREATE_RAW_PATH:
        body = createtask()
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


def gettask():
    "To retrive the task from DynamoDB"
    body = 'Hello Lambda from get task'
    return body
    
    
def createtask():
    "To add the task info into the DynamoDB"
    body = 'Hello Lambda from create task'
    return body
    
    
