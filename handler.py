import requests

API_URL = "https://api.quotable.io/quotes/random"

def main_handler(event, context):
    res = requests.get(API_URL)

    if res.status_code != requests.codes.get("ok"):
        print(res.json())

        return {
            "statusCode": requests.codes.get("server_error"),
            "body": "We have a problem"
        }

    return {
        "statusCode": requests.codes.get("ok"),
        "body": res.json()
    }
