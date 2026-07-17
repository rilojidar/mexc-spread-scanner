from config import TRADE_AMOUNT


def show_signal(symbol, side, price, take_profit, stop_loss):

    print("==========================")
    print("   SINYAL TRADING MEXC")
    print("==========================")

    print("PAIR        :", symbol)
    print("ARAH        :", side)
    print("ENTRY       :", price)
    print("MODAL       :", TRADE_AMOUNT)
    print("TAKE PROFIT :", take_profit)
    print("STOP LOSS   :", stop_loss)

    print("==========================")
    print("MENUNGGU KEPUTUSAN MANUAL")
    print("==========================")



def close_signal(symbol):

    print("==========================")
    print("TUTUP POSISI MANUAL")
    print("PAIR :", symbol)
    print("==========================")
