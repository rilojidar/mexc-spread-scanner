from mexc_api import get_all_bid_ask


def calculate_spread(bid, ask):

    if bid <= 0:
        return 0

    return ((ask - bid) / bid) * 100



def scan_spread():

    markets = get_all_bid_ask()

    results = []


    print("Jumlah pair:", len(markets))


    for symbol, data in markets.items():

        try:

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


        except:

            continue



    results.sort(
        key=lambda x: x["spread"],
        reverse=True
    )


    return results
