from config import TEST_MODE, TRADE_AMOUNT


def open_position(symbol, side, price):

    print("======================")
    print("OPEN POSITION")
    print("Symbol :", symbol)
    print("Side   :", side)
    print("Price  :", price)
    print("Amount :", TRADE_AMOUNT)
    print("======================")


    if TEST_MODE:
        print("MODE TEST - ORDER TIDAK DIKIRIM")
        return {
            "status": "SIMULATION",
            "symbol": symbol,
            "side": side,
            "price": price
        }


    # Nanti bagian API order MEXC masuk di sini

    return {
        "status": "REAL ORDER",
        "symbol": symbol,
        "side": side,
        "price": price
    }



def close_position(symbol):

    print("======================")
    print("CLOSE POSITION")
    print("Symbol :", symbol)
    print("======================")


    return {
        "status": "CLOSED",
        "symbol": symbol
    }



if __name__ == "__main__":

    test = open_position(
        "BTCUSDT",
        "LONG",
        60000
    )

    print(test)
