import requests
import hmac
import hashlib

from config import API_KEY, SECRET_KEY


BASE_URL = "https://api.mexc.com"


def get_orderbook(symbol):

    try:

        url = BASE_URL + "/api/v3/ticker/bookTicker"

        params = {
            "symbol": symbol
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()


        bid = float(data["bidPrice"])
        ask = float(data["askPrice"])


        return {
            "symbol": symbol,
            "bid": bid,
            "ask": ask
        }


    except Exception as e:

        print(
            "ORDERBOOK ERROR",
            symbol,
            e
        )

        return None



def get_price(symbol):

    data = get_orderbook(symbol)

    if data:
        return data["ask"]

    return None



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
