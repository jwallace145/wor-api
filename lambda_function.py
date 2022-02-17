import json
from src.aws_gateways.dynamodb_gateway import DynamoDbGateway


def lambda_handler(event, context):

    dynamodb_gateway = DynamoDbGateway()

    dynamodb_gateway.get_strike_prices(email="jimmy.wallace145@gmail.com")

    return {"statusCode": 200, "body": json.dumps("wor-api")}


lambda_handler(event=None, context=None)
