from dataclasses import dataclass
from typing import Literal
from src.utils.logger import Logger


log = Logger(__name__).get_logger()


@dataclass
class EventParser:

    event: dict
    method: Literal["GET", "POST"] = None
    path: str = None

    def __post_init__(self) -> None:
        self.method = self.event.get("httpMethod")
        self.path = self.event.get("path")

    def get_method(self) -> str:
        log.info(f"the method of the event: {self.method}")
        return self.method

    def get_path(self) -> str:
        log.info(f"the path of the event: {self.path}")
        return self.path
