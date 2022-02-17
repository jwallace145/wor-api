import json
from src.aws_gateways.dynamodb_gateway import DynamoDbGateway

from src.utils.logger import Logger

log = Logger(__name__).get_logger()


def lambda_handler(event, context):

    log.info(f"lambda event:\n{json.dumps(event, indent=4)}")
    log.info(f"lambda context:\n{json.dumps(context, indent=4)}")

    dynamodb_gateway = DynamoDbGateway()

    dynamodb_gateway.get_strike_prices(email="jimmy.wallace145@gmail.com")

    return {"statusCode": 200, "body": json.dumps("wor-api")}


lambda_handler(event=None, context=None)
