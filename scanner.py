from mexc_api import get_all_symbols, get_bid_ask


def calculate_spread(bid, ask):

    if bid <= 0:
        return 0

    spread = ((ask - bid) / bid) * 100

    return spread



def scan_spread():

    symbols = get_all_symbols()

    results = []


    print("Jumlah pair:", len(symbols))


    for symbol in symbols:

        try:

            data = get_bid_ask(symbol)

            bid = data["bid"]
            ask = data["ask"]


            spread = calculate_spread(
                bid,
                ask
            )


            results.append({
                "symbol": symbol,
                "bid": bid,
                "ask": ask,
                "spread": spread
            })


        except Exception:

            continue



    results.sort(
        key=lambda x: x["spread"],
        reverse=True
    )


    return results
