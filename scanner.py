from mexc_api import get_all_bid_ask, get_all_volume, get_order_depth


MIN_VOLUME = 100000
CHECK_DEPTH = 20



def calculate_spread(bid, ask):

    if bid <= 0:
        return 0

    return ((ask - bid) / bid) * 100



def scan_spread():

    markets = get_all_bid_ask()

    volumes = get_all_volume()

    results = []


    print("Jumlah pair:", len(markets))


    # tahap 1: scan cepat semua pair

    for symbol, data in markets.items():

        try:

            volume = volumes.get(symbol, 0)


            if volume < MIN_VOLUME:
                continue


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
                "spread": spread,
                "volume": volume

            })


        except:

            continue



    # urutkan spread terbesar

    results.sort(
        key=lambda x: x["spread"],
        reverse=True
    )



    # tahap 2: cek depth hanya kandidat teratas

    final_results = []


    for item in results[:CHECK_DEPTH]:

        try:

            depth = get_order_depth(
                item["symbol"]
            )


            item["bid_depth"] = depth["bid_depth"]
            item["ask_depth"] = depth["ask_depth"]


            final_results.append(item)


        except:

            continue



    return final_results
