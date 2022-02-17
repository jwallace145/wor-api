from dataclasses import dataclass
from typing import List

from src.models.strike_price import StrikePrice


@dataclass
class User:

    email: str
    strike_prices: List[StrikePrice]
