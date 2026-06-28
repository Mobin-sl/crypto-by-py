import requests
from datetime import datetime
from config import COINS
# linke api
#mitonim az api haye digar ham estefade konim
URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_prices():

    ids = ",".join(COINS.keys())

    params = {
        "ids": ids,
        "vs_currencies": "usd"
    }

    response = requests.get(URL, params=params, timeout=20)
    data = response.json()
    result = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin_id, symbol in COINS.items():

        price = data.get(coin_id, {}).get("usd", "N/A")

        result.append({
            "Time": now,
            "Symbol": symbol,
            "Coin": coin_id,
            "Price(USD)": price
        })

    return result