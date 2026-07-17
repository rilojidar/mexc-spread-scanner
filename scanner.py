import time
from config import SYMBOLS, MIN_SPREAD
from mexc_api import get_price


def check_spread(symbol):

    try:

        price = get_price(symbol)

        # simulasi bid dan ask sederhana
        bid = price * 0.999
        ask = price * 1.001

        spread = ((ask - bid) / bid) * 100

        return {
            "symbol": symbol,
            "bid": bid,
            "ask": ask,
            "spread": spread
        }

    except Exception as e:

        return {
            "symbol": symbol,
            "error": str(e)
        }



def scan_market():

    results = []

    for symbol in SYMBOLS:

        data = check_spread(symbol)

        if "spread" in data:

            if data["spread"] >= MIN_SPREAD:
                results.append(data)

    return results



if __name__ == "__main__":

    print("START SCANNER")

    while True:

        opportunities = scan_market()

        for item in opportunities:
            print(
                item["symbol"],
                "Spread:",
                round(item["spread"],4),
                "%"
            )

        time.sleep(10)
