from app import app
import time, requests
from datetime import datetime
from retry import retry


@app.template_filter("uptime")
def uptime(startTime):
    d1 = datetime.fromtimestamp(startTime).strftime("%Y-%m-%d %H:%M:%S")
    d2 = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")

    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

    diff = d2 - d1
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days}d {hours % 24}h {minutes}m {seconds}s"


@app.template_filter("epochToDatetime")
def epochToDatetime(epoch):
    return datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")


@app.template_filter("removeHashrateM")
def removeHashrateM(hashrate):
    return hashrate.split(" ")[0]


LAST_UPDATE = 0
LAST_VALUE = {"ethereum": {"eur": 0}, "zilliqa": {"eur": 0}}
@app.template_filter("convToEur")
def convToEur(amount, coin):
    global LAST_UPDATE
    global LAST_VALUE
    if time.time() - LAST_UPDATE > 5:
        LAST_UPDATE = time.time()
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum%2Czilliqa&vs_currencies=eur"
        response = requests.get(url)
        if response.status_code == 200:
            LAST_VALUE = response.json()

    if coin == "eth":
        return round(amount * LAST_VALUE["ethereum"]["eur"], 2)
    elif coin == "zil":
        return round(amount * LAST_VALUE["zilliqa"]["eur"], 2)