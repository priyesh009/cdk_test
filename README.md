
# Task Manager service

##  Objectives
Goal is to create task manager service in AWS

## Techinical Details
AWS CDK is being used to create the required Task Manager service resources.

### Below Resource are being created using AWS CDK(Python) 
- AWS Lambda
- AWS API HTTP Gateway and its routes
- DynamoDB Table

### Pending Tasks
- Complete the lambda script and test the logic to inject and retrive task information 
- set dynamoDb table name in the env variable of AWS lambda
- create Lambda Role in CDK and grant Put and get DynamoDB permissions.
- Configuring access patterns
- Error/Exception handling
- Final testing and making the code prod ready