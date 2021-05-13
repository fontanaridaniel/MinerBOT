from app import app
from flask import render_template
import requests, time
from app.functions import *


@app.route("/updatebalance", methods=["POST"])
def updateBalance():
    url = "https://billing.ezil.me/balances/0x1c968c05c64964da8146031dbe9e2e21d3b6432c.zil17djp4ds0f6w47d66lyktmgtsx7naf8jl5wr948"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            return render_template(
                "/components/balanceComponent.html",
                eth=round(response.json()["eth"], 6),
                zil=round(response.json()["zil"], 6),
            )


@app.route("/updateworkersonline", methods=["POST"])
def updateWorkersOnline():
    workersState = getWorkersState()

    workersOnline = 0
    for worker in workersState:
        currentTime = time.time()
        if currentTime - worker["last_update"] < 10:
            workersOnline += 1
    return render_template(
        "/components/workersOnlineComponent.html", workersOnline=workersOnline
    )


@app.route("/updateworkersstate", methods=["POST"])
def updateWorkersState():
    workersState = getWorkersState()

    total = {
        "hashrate": 0,
        "accepted_shares": 0,
        "rejected_shares": 0,
        "invalid_shares": 0,
        "power": 0,
    }
    for worker in workersState:
        currentTime = time.time()
        for gpu in worker["miner"]["devices"]:
            if currentTime - worker["last_update"] < 10:
                total["hashrate"] += float(gpu["hashrate"].split(" ")[0])
                total["hashrate"] = round(total["hashrate"], 2)
                total["accepted_shares"] += int(gpu["accepted_shares"])
                total["rejected_shares"] += int(gpu["rejected_shares"])
                total["invalid_shares"] += int(gpu["invalid_shares"])
                total["power"] += int(gpu["power"])

    return render_template(
        "/components/workersStateComponent.html",
        workersState=workersState,
        currentTime=time.time(),
        total=total,
    )


@app.route("/updatemonthearningscomparison", methods=["POST"])
def updateMonthWarningsComparison():
    earningData = getEarningsData()
    start = [earningData[0][1], earningData[0][2]]
    current = [earningData[-1][1], earningData[-1][2]]

    ethEarn = current[0] - start[0]
    zilEarn = current[1] - start[1]

    if current[0] < start[0]:
        for index, _ in enumerate(earningData):
            if earningData[index][1] < earningData[index - 1][1]:
                ethEarn = (
                    float(current[0]) + float(earningData[index - 1][1])
                ) - float(start[0])

    if current[1] < start[1]:
        for index, _ in enumerate(earningData):
            if earningData[index][2] < earningData[index - 1][2]:
                zilEarn = (
                    float(current[1]) + float(earningData[index - 1][2])
                ) - float(start[1])

    return render_template(
        "/components/monthEarningsComparisonComponent.html",
        start=start,
        current=current,
        ethEarn=ethEarn,
        zilEarn=zilEarn,
    )


@app.route("/updateworkersearnings", methods=["POST"])
def updateWorkersEarnings():
    data = getAllWorkersData()
    currentETH = getEarningsData()[-1][1]
    workDone = getWorkDone()
    powerMedian = getPowerMedian()
    hashrateMedian = getHashrateMedian()

    totalHashrate = 0
    for worker in data:
        totalHashrate += (
            hashrateMedian[worker["worker"][0]] * 60 * workDone[worker["worker"][0]]
        )

    totalData = []
    for worker in data:
        workerData = {}
        workerData["worker"] = worker["worker"][0]
        workerData["minutes"] = workDone[workerData["worker"]]
        workerData["powerMedian"] = powerMedian[workerData["worker"]]
        workerData["hashrateMedian"] = hashrateMedian[workerData["worker"]]
        workerData["powerPrice"] = ((powerMedian[workerData["worker"]] * 0.26) / 1000) * (workerData["minutes"] / 60)
        workerData["%"] = (
            (workerData["hashrateMedian"] * 60 * workerData["minutes"])
            / totalHashrate
            * 100
        )
        workerData["ETH"] = currentETH / 100 * workerData["%"]

        totalData.append(workerData)

    return render_template(
        "/components/workersEarningsComponent.html", totalData=totalData
    )
