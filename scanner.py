from config import SYMBOLS, MIN_SPREAD, BUY_FEE, SELL_FEE, MIN_NET_PROFIT
from mexc_api import get_price


def check_market(symbol):

    try:

        price = get_price(symbol)

        # simulasi harga bid dan ask
        bid = price * 0.9995
        ask = price * 1.0005


        # hitung spread kotor
        spread = ((ask - bid) / bid) * 100


        # hitung total fee beli + jual
        total_fee = BUY_FEE + SELL_FEE


        # perkiraan profit bersih
        net_profit = spread - total_fee


        print(
            symbol,
            "| Harga:",
            price,
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

        print(symbol, "ERROR:", e)

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
