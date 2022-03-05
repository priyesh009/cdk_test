from aws_cdk import core as cdk
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigatewayv2 as apigateway
from aws_cdk import aws_apigatewayv2_integrations as api_integrations
from aws_cdk import aws_dynamodb as dynamodb
#from aws_cdk import aws_s3 as s3
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

DYNAMODB_TABLE = 'TMS_DyDB'

class CdkTestStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket = s3.Bucket(self, 'sitebucket', bucket_name = 'pricdks3bucket', public_read_access = True)
        # core.CfnOutput(self,'sitebucketname', value=bucket.bucket_name)

        # Defines an AWS Lambda resource
        tms_lambda = _lambda.Function(
            self, 'TMS',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='tms.lambda_handler',
            environment={
            "tms_table": DYNAMODB_TABLE
    }
        )
        # Defines an AWS HTTP API GW resource
        tms_httpapi = apigateway.HttpApi(self,
                                            "tmsHttpApi",
                                            cors_preflight={
                                            "allow_methods": [apigateway.HttpMethod.GET, apigateway.HttpMethod.HEAD, apigateway.HttpMethod.OPTIONS, apigateway.HttpMethod.POST],
                                            "allow_origins": ["*"],
                                            "max_age": core.Duration.days(10)
                                            },
                                            # default_domain_mapping={
                                            # "domain_name": dn,
                                            # },
                                            )
        # Defines an AWS HTTP API GW integration with Lambda resource
        tms_integration = api_integrations.LambdaProxyIntegration(
                            handler=tms_lambda,
                            )
        # Add AWS HTTP API GW POST task Routes
        tms_httpapi.add_routes(
                path="/createtask",
                methods=[apigateway.HttpMethod.POST],
                integration=tms_integration
                ) 
        # Add AWS HTTP API GW POST task Routes
        tms_httpapi.add_routes(
                path="/gettask",
                methods=[apigateway.HttpMethod.GET],
                integration=tms_integration
                ) 

        # Defines an AWS DynamoDB Table resource
        tmstable = dynamodb.Table(self, "tmsTable", table_name = DYNAMODB_TABLE,
                partition_key=dynamodb.Attribute(name="PK", type=dynamodb.AttributeType.STRING),
                sort_key=dynamodb.Attribute(name="SK", type=dynamodb.AttributeType.STRING)
            )