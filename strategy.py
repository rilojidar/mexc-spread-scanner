from config import TAKE_PROFIT, STOP_LOSS


def decide_trade(signal):

    """
    Menentukan arah posisi:
    LONG  = beli berharap naik
    SHORT = jual berharap turun
    """

    spread = signal.get("spread", 0)


    if spread <= 0:
        return None


    # Strategi dasar
    # Jika spread memenuhi syarat, ambil posisi

    if spread >= 0.3:

        return {
            "action": "LONG",
            "symbol": signal["symbol"],
            "entry": signal["ask"],
            "take_profit": signal["ask"] * (1 + TAKE_PROFIT / 100),
            "stop_loss": signal["ask"] * (1 - STOP_LOSS / 100)
        }


    return None



def check_exit(position, current_price):

    if position["action"] == "LONG":

        if current_price >= position["take_profit"]:
            return "TAKE_PROFIT"


        if current_price <= position["stop_loss"]:
            return "STOP_LOSS"


    return "HOLD"
