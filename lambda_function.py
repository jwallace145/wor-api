import json
from src.handlers.event_handler import EventHandler
from src.utils.event_parser import EventParser

from src.utils.logger import Logger

log = Logger(__name__).get_logger()


def lambda_handler(event, context):

    log.info(f"lambda event:\n{json.dumps(event, indent=4)}")

    event_parser = EventParser(event)

    event_handler = EventHandler(
        method=event_parser.get_method(), path=event_parser.get_path()
    )

    response = event_handler.handle()

    return {"statusCode": 200, "body": json.dumps(response)}


lambda_handler(event=None, context=None)
