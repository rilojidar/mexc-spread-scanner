from mexc_api import get_all_bid_ask, get_all_volume


# minimal volume transaksi 24 jam (USDT)
MIN_VOLUME = 100000



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


            # buang pair terlalu sepi
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



    results.sort(
        key=lambda x: x["spread"],
        reverse=True
    )


    return results
