import os, json, time, os.path
import pandas as pd
from datetime import datetime

os.system("cls")

PATH = f"{os.path.abspath(os.path.dirname(__file__))}"
while True:
    if datetime.now().second == 0:
        for file in os.listdir(f"{PATH}/json/workers/"):
            data = json.load(open(f"{PATH}/json/workers/{file}"))
            for gpu in data["miner"]["devices"]:
                if time.time() - data["last_update"] < 10:
                    dataArray = [
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        data["stratum"]["user"].split(".")[-1],
                        gpu["id"],
                        gpu["info"],
                        gpu["hashrate"].split(" ")[0],
                        gpu["accepted_shares"],
                        gpu["temperature"],
                        gpu["fan"],
                        gpu["power"],
                        gpu["core_clock"],
                        gpu["mem_clock"],
                    ]
                else:
                    dataArray = [
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        data["stratum"]["user"].split(".")[-1],
                        gpu["id"],
                        gpu["info"],
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ]
                df = pd.DataFrame([dataArray], columns=["datetime","worker","id","gpu","hashrate","accepted_shares","temperature","fan","power","core_clock","mem_clock"])
                if os.path.isfile(f"""{PATH}/csv/workers/{data["stratum"]["user"].split(".")[-1]}.csv"""):
                    df.to_csv(f"""{PATH}/csv/workers/{data["stratum"]["user"].split(".")[-1]}.csv""", mode="a", header=False, index=False)
                else:
                    df.to_csv(f"""{PATH}/csv/workers/{data["stratum"]["user"].split(".")[-1]}.csv""", index=False)
        print(f"> Saved workers data: {datetime.now()}")
        time.sleep(50)