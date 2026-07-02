import json

from shared.aws_clients import s3
from shared.dynamodb_helper import get_table
from shared.logger import logger
from shared.responses import success
from shared.s3_helper import read_json

from parser import parse_earthquake


def lambda_handler(event, context):
    try:
        logger.info(f"Incoming Event: {json.dumps(event)}")

        record = event["Records"][0]

        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        logger.info(f"Bucket: {bucket}")
        logger.info(f"Key: {key}")

        earthquake = read_json(s3, bucket, key)

        item = parse_earthquake(earthquake)

        table = get_table("earthquake")

        table.put_item(Item=item)

        logger.info("Earthquake data stored successfully!")

        return success("Earthquake data stored successfully!")

    except Exception as e:
        logger.error(f"Earthquake Error: {e}")
        raise