from config import SYMBOLS, MIN_SPREAD, BUY_FEE, SELL_FEE, MIN_NET_PROFIT
from mexc_api import get_orderbook


def check_market(symbol):

    try:

        market = get_orderbook(symbol)

        if not market:
            return None


        bid = market["bid"]
        ask = market["ask"]


        # spread nyata dari order book
        spread = ((bid - ask) / ask) * 100


        # ubah jadi nilai positif
        spread = abs(spread)


        # total fee beli + jual
        total_fee = BUY_FEE + SELL_FEE


        # perkiraan profit bersih
        net_profit = spread - total_fee


        print(
            symbol,
            "| Bid:",
            bid,
            "| Ask:",
            ask,
            "| Spread:",
            round(spread, 4),
            "%",
            "| Net:",
            round(net_profit, 4),
            "%"
        )


        return {
            "symbol": symbol,
            "bid": bid,
            "ask": ask,
            "spread": spread,
            "net_profit": net_profit
        }


    except Exception as e:

        print(
            symbol,
            "ERROR:",
            e
        )

        return None



def scan_market():

    results = []


    for symbol in SYMBOLS:

        data = check_market(symbol)


        if data:

            if (
                data["spread"] >= MIN_SPREAD
                and
                data["net_profit"] >= MIN_NET_PROFIT
            ):

                results.append(data)


    return results
