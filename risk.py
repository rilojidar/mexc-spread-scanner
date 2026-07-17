from config import TRADE_AMOUNT


def calculate_position():

    """
    Menghitung ukuran posisi
    berdasarkan modal yang ditentukan
    """

    return TRADE_AMOUNT



def check_risk(balance):

    """
    Cek apakah saldo cukup
    """

    if balance >= TRADE_AMOUNT:

        return True

    return False



def risk_report(position):

    print("======================")
    print("RISK REPORT")
    print("Symbol :", position.get("symbol"))
    print("Side   :", position.get("side"))
    print("Amount :", position.get("amount"))
    print("======================")
