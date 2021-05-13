import os, time, os.path ,requests
import pandas as pd
from datetime import datetime

os.system("cls")

PATH = f"{os.path.abspath(os.path.dirname(__file__))}"
while True:
    if datetime.now().second == 0:
        url = "https://billing.ezil.me/balances/0x1c968c05c64964da8146031dbe9e2e21d3b6432c.zil17djp4ds0f6w47d66lyktmgtsx7naf8jl5wr948"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            dataArray = [
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                round(data["eth"], 6),
                round(data["zil"], 6),
            ]
            df = pd.DataFrame([dataArray], columns=["datetime","eth","zil"])
            if os.path.isfile(f"{PATH}/csv/balance/balance.csv"):
                df.to_csv(f"{PATH}/csv/balance/balance.csv", mode="a", header=False, index=False)
            else:
                df.to_csv(f"{PATH}/csv/balance/balance.csv", index=False)
            print(f"> Saved balance data: {datetime.now()}")
            time.sleep(50)