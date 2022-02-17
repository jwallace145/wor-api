from dataclasses import dataclass


@dataclass
class StrikePrice:

    symbol: str
    buy_price: float
    sell_price: float
