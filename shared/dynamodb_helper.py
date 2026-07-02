from shared.aws_clients import dynamodb
from shared.config import TABLES


def get_table(name):
    return dynamodb.Table(TABLES[name])