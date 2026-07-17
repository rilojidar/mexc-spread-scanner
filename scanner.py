from mexc_api import get_all_bid_ask, get_all_volume, get_order_depth


MIN_VOLUME = 100000
MIN_DEPTH = 1000



def calculate_spread(bid, ask):

    if bid <= 0:
        return 0

    return ((ask - bid) / bid) * 100



def scan_spread():

    markets = get_all_bid_ask()

    volumes = get_all_volume()

    results = []


    print("Jumlah pair:", len(markets))


    for symbol, data in markets.items():

        try:

            if symbol not in volumes:
                continue


            volume = volumes[symbol]


            if volume < MIN_VOLUME:
                continue


            bid = data["bid"]
            ask = data["ask"]


            depth = get_order_depth(symbol)


            bid_depth = depth["bid_depth"]
            ask_depth = depth["ask_depth"]


            if (
                bid_depth < MIN_DEPTH
                or
                ask_depth < MIN_DEPTH
            ):
                continue


            spread = calculate_spread(
                bid,
                ask
            )


            results.append({

                "symbol": symbol,
                "bid": bid,
                "ask": ask,
                "spread": spread,
                "volume": volume,
                "bid_depth": bid_depth,
                "ask_depth": ask_depth

            })


        except:

            continue



    results.sort(
        key=lambda x: x["spread"],
        reverse=True
    )


    return results
