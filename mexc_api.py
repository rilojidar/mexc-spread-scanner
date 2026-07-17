import requests


BASE_URL = "https://api.mexc.com"


def get_all_symbols():

    url = BASE_URL + "/api/v3/exchangeInfo"

    response = requests.get(url, timeout=10)

    data = response.json()

    symbols = []

    for item in data["symbols"]:

        symbol = item["symbol"]

        if (
            symbol.endswith("USDT")
            and item["status"] == "1"
        ):
            symbols.append(symbol)

    return symbols



def get_bid_ask(symbol):

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

    return {
        "symbol": symbol,
        "bid": float(data["bidPrice"]),
        "ask": float(data["askPrice"])
    }
