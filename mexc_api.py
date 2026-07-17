import requests
import time
import hmac
import hashlib
from config import API_KEY, SECRET_KEY


BASE_URL = "https://api.mexc.com"


def get_price(symbol):

    url = BASE_URL + "/api/v3/ticker/price"

    params = {
        "symbol": symbol
    }

    response = requests.get(url, params=params)

    data = response.json()

    return float(data["price"])



def create_signature(query_string):

    signature = hmac.new(
        SECRET_KEY.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    return signature



def server_time():

    url = BASE_URL + "/api/v3/time"

    response = requests.get(url)

    return response.json()



if __name__ == "__main__":

    print("MEXC API CONNECTED")

    print(server_time())
