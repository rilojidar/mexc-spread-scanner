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
