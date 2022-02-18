from dataclasses import dataclass
from typing import Literal
from src.handlers.strike_prices_handler import StrikePriceHandler
from src.utils.logger import Logger

log = Logger(__name__).get_logger()


@dataclass
class EventHandler:

    method: Literal["GET", "POST"]
    path: str
    query_string_params: dict
    strike_prices_handler: StrikePriceHandler = StrikePriceHandler()

    def handle(self) -> None:
        if self.method == "GET" and self.path.startswith("/strike-prices"):
            email = self.query_string_params.get("email", "email not defined")
            log.info(f"Handling getting strike prices for email {email}.....")
            return self.strike_prices_handler.get_strike_prices(email=email)
