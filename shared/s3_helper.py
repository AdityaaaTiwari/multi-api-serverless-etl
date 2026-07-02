import json


def read_json(s3, bucket, key):
    """
    Read a JSON file from S3 and return it as a Python dictionary.
    """
    response = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(response["Body"].read())