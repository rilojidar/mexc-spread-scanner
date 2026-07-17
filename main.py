import time

from scanner import scan_market
from strategy import decide_trade
from trader import open_position
from risk import calculate_position


def run_bot():

    print("======================")
    print("MEXC TWO WAY BOT START")
    print("======================")


    while True:

        try:

            # scan peluang
            signals = scan_market()


            if signals:

                for signal in signals:

                    print("Signal ditemukan:")
                    print(signal)


                    # tentukan posisi
                    decision = decide_trade(signal)


                    if decision:

                        amount = calculate_position()


                        order = open_position(
                            decision["symbol"],
                            decision["action"],
                            decision["entry"]
                        )


                        print(order)


            else:

                print("Belum ada peluang...")


            time.sleep(10)


        except Exception as e:

            print("ERROR:", e)

            time.sleep(10)



if __name__ == "__main__":

    run_bot()
