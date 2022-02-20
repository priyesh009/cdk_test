from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as _lambda
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkTestStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 'sitebucket', bucket_name = 'pricdks3bucket', public_read_access = True)
        core.CfnOutput(self,'sitebucketname', value=bucket.bucket_name)
        # The code that defines your stack goes here

                # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'TMS',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='tms.lambda_handler',
        )