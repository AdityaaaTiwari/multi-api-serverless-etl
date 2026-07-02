def success(message):
    return {
        "statusCode": 200,
        "body": message
    }


def failure(message):
    return {
        "statusCode": 500,
        "body": message
    }