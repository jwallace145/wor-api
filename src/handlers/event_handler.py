from dataclasses import dataclass
from typing import Literal
from src.handlers.strike_prices_handler import StrikePriceHandler


@dataclass
class EventHandler:

    method: Literal["GET", "POST"]
    path: str
    strike_prices_handler: StrikePriceHandler = StrikePriceHandler()

    def get_strike_prices(self, emaiL: str):
        self.strike_prices_handler.get_all_strike_prices

    def handle(self) -> None:
        if self.method == "GET" and self.path.startswith("/strike-prices"):
            return self.strike_prices_handler.get_strike_prices(
                email="jimmy.wallace145@gmail.com"
            )
