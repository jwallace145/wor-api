from dataclasses import dataclass

from src.aws_gateways.dynamodb_gateway import DynamoDbGateway
from src.models.strike_price import StrikePrice
from typing import List
from src.utils.logger import Logger

log = Logger(__name__).get_logger()


@dataclass
class StrikePriceHandler:

    dynamodb_gateway: DynamoDbGateway = DynamoDbGateway()

    def get_strike_prices(self, email: str) -> List[StrikePrice]:
        strike_prices = self.dynamodb_gateway.get_strike_prices(email=email)
        strike_prices = [vars(strike_price) for strike_price in strike_prices]
        return [vars(strike_price) for strike_price in strike_prices]
