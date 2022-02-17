import json
from src.handlers.event_handler import EventHandler
from src.utils.event_parser import EventParser

from src.utils.logger import Logger

log = Logger(__name__).get_logger()


def lambda_handler(event, context):

    log.info(f"lambda event:\n{json.dumps(event)}")

    event_parser = EventParser(event)

    event_handler = EventHandler(
        method=event_parser.get_method(), path=event_parser.get_path()
    )

    response = event_handler.handle()

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(response),
    }
