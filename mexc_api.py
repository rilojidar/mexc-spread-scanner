import requests


BASE_URL = "https://api.mexc.com"



def get_all_symbols():

    url = BASE_URL + "/api/v3/exchangeInfo"

    response = requests.get(
        url,
        timeout=10
    )

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



def get_all_bid_ask():

    """
    Mengambil semua bid/ask sekaligus
    """

    url = BASE_URL + "/api/v3/ticker/bookTicker"


    response = requests.get(
        url,
        timeout=10
    )


    data = response.json()


    markets = {}


    for item in data:

        symbol = item["symbol"]


        if symbol.endswith("USDT"):

            try:

                markets[symbol] = {
                    "bid": float(item["bidPrice"]),
                    "ask": float(item["askPrice"])
                }


            except:

                continue


    return markets
def get_all_volume():

    url = BASE_URL + "/api/v3/ticker/24hr"

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()


    volumes = {}


    for item in data:

        symbol = item["symbol"]


        if symbol.endswith("USDT"):

            try:

                volumes[symbol] = float(
                    item["quoteVolume"]
                )

            except:

                continue


    return volumes
def get_order_depth(symbol):

    url = BASE_URL + "/api/v3/depth"

    params = {
        "symbol": symbol,
        "limit": 5
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    data = response.json()


    bid_price = float(data["bids"][0][0])
    bid_amount = float(data["bids"][0][1])

    ask_price = float(data["asks"][0][0])
    ask_amount = float(data["asks"][0][1])


    bid_value = bid_price * bid_amount
    ask_value = ask_price * ask_amount


    return {
        "bid_depth": bid_value,
        "ask_depth": ask_value
    }
