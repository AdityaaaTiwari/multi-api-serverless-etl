import json

from shared.aws_clients import s3
from shared.dynamodb_helper import get_table
from shared.logger import logger
from shared.responses import success
from shared.s3_helper import read_json

from parser import parse_transit


def lambda_handler(event, context):
    try:
        logger.info(f"Incoming Event: {json.dumps(event)}")

        record = event["Records"][0]

        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        logger.info(f"Bucket: {bucket}")
        logger.info(f"Key: {key}")

        transit = read_json(s3, bucket, key)

        item = parse_transit(transit)

        table = get_table("transit")

        table.put_item(Item=item)

        logger.info("Transit data stored successfully!")

        return success("Transit data stored successfully!")

    except Exception as e:
        logger.error(f"Transit Error: {e}")
        raise