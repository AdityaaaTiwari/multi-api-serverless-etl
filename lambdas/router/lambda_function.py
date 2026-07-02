import json

from shared.aws_clients import lambda_client
from shared.config import ROUTES
from shared.logger import logger
from shared.responses import success


def lambda_handler(event, context):
    try:
        logger.info(f"Incoming Event: {json.dumps(event)}")

        record = event["Records"][0]
        key = record["s3"]["object"]["key"].lower()

        logger.info(f"Uploaded File: {key}")

        target = None

        for folder, function_name in ROUTES.items():
            if folder in key:
                target = function_name
                break

        if target is None:
            raise Exception("No matching Lambda found.")

        logger.info(f"Target Lambda: {target}")

        response = lambda_client.invoke(
            FunctionName=target,
            InvocationType="Event",
            Payload=json.dumps(event),
        )

        logger.info(f"Invoke Response: {response}")

        return success(f"{target} invoked successfully")

    except Exception as e:
        logger.error(f"Router Error: {e}")
        raise