import boto3

s3 = boto3.client("s3")
lambda_client = boto3.client("lambda")
dynamodb = boto3.resource("dynamodb")