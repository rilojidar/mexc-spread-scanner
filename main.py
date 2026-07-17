import time

from scanner import scan_market
from strategy import decide_trade
from trader import show_signal


def run_bot():

    print("==============================")
    print(" MEXC MANUAL SIGNAL BOT START ")
    print("==============================")


    while True:

        try:

            signals = scan_market()


            if signals:

                for signal in signals:

                    decision = decide_trade(signal)


                    if decision:

                        show_signal(
                            decision["symbol"],
                            decision["action"],
                            decision["entry"],
                            decision["take_profit"],
                            decision["stop_loss"]
                        )

            else:

                print("Belum ada sinyal...")


            time.sleep(10)


        except Exception as e:

            print("ERROR:", e)

            time.sleep(10)



if __name__ == "__main__":

    run_bot()
