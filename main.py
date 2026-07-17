import time

from scanner import scan_spread


def run():

    print("==============================")
    print(" MEXC SPREAD SCANNER START ")
    print("==============================")


    while True:

        try:

            results = scan_spread()


            print("\nTOP SPREAD TERBESAR")
            print("==============================")


            for item in results[:20]:

                print(
                    item["symbol"],
                    "| Bid:",
                    item["bid"],
                    "| Ask:",
                    item["ask"],
                    "| Spread:",
                    round(item["spread"], 4),
                    "%"
                )


            print("==============================")
            print("Refresh 30 detik...\n")


            time.sleep(30)


        except Exception as e:

            print("ERROR:", e)

            time.sleep(30)



if __name__ == "__main__":

    run()
