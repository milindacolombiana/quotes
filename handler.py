import logging
import requests
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


API_URL = os.getenv("API_URL")

def main_handler(event, context):
    res = requests.get(API_URL)

    logger.info("url: %s, status code: %d", API_URL, res.status_code)

    if res.status_code != requests.codes.get("ok"):
        logger.error("there was en error in the request, body: %s", res.json())

        return {
            "statusCode": requests.codes.get("server_error"),
            "body": "We have a problem"
        }

    return {
        "statusCode": requests.codes.get("ok"),
        "body": res.json()
    }


(main_handler(None, None))
