from dataclasses import dataclass

import boto3
import os
from mypy_boto3_dynamodb import DynamoDBClient
from typing import List

from src.models.strike_price import StrikePrice
from src.utils.logger import Logger

log = Logger(__name__).get_logger()

TABLE_NAME = os.getenv("TABLE_NAME")


@dataclass
class DynamoDbGateway:

    client: DynamoDBClient = boto3.client(
        "dynamodb", region_name=os.getenv("AWS_REGION")
    )

    def get_strike_prices(self, email: str) -> List[StrikePrice]:
        log.info(f"getting strike prices for email {email}.....")
        strike_prices_db = self.client.get_item(
            TableName=TABLE_NAME, Key={"email": {"S": email}}
        )["Item"]["strike_prices"]["L"]
        strike_prices = []
        for prices in strike_prices_db:
            strike_price = StrikePrice(
                symbol=prices["M"]["symbol"]["S"],
                buy_price=prices["M"]["buy_price"]["N"],
                sell_price=prices["M"]["sell_price"]["N"],
            )
            log.info(f"email {email} strike price: {strike_price}")
            strike_prices.append(strike_price)
        return strike_prices
