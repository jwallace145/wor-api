from dataclasses import dataclass
from typing import Literal
from src.handlers.strike_prices_handler import StrikePriceHandler


@dataclass
class EventHandler:

    method: Literal["GET", "POST"]
    path: str
    query_string_params: dict
    strike_prices_handler: StrikePriceHandler = StrikePriceHandler()

    def handle(self) -> None:
        if self.method == "GET" and self.path.startswith("/strike-prices"):
            return self.strike_prices_handler.get_strike_prices(
                email=self.query_string_params.get("email")
            )
