import time
from config import SYMBOLS, MIN_SPREAD
from mexc_api import get_price


def check_market(symbol):

    try:

        price = get_price(symbol)

        # simulasi bid dan ask dari harga pasar
        bid = price * 0.9995
        ask = price * 1.0005

        spread = ((ask - bid) / bid) * 100


        print(
            symbol,
            "| Harga:",
            price,
            "| Spread:",
            round(spread, 4),
            "%"
        )


        return {
            "symbol": symbol,
            "bid": bid,
            "ask": ask,
            "spread": spread
        }


    except Exception as e:

        print(symbol, "ERROR:", e)

        return None



def scan_market():

    results = []


    for symbol in SYMBOLS:

        data = check_market(symbol)


        if data:

            if data["spread"] >= MIN_SPREAD:

                results.append(data)


    return results
