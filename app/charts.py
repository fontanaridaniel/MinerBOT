from app import app
from app.functions import *

COLORS = [
    "rgba(0, 176, 255, 0.8)",
    "rgba(255, 196, 0, 0.8)",
    "rgba(245, 0, 87, 0.8)",
    "rgba(101, 31, 255, 0.8)",
    "rgba(0, 230, 118, 0.8)",
    "rgba(143, 45, 86, 0.8)",
    "rgba(100, 245, 141, 0.8)",
    "rgba(200, 70, 48, 0.8)",
    "rgba(4, 150, 255, 0.8)",
]


@app.route("/updatehashratechart", methods=["POST"])
def updateHashRateChart():
    last24hData = getLast24hData()
    labels = []
    for label in last24hData[0]:
        labels.append(label[0])

    datasets = []
    for index, worker in enumerate(last24hData):
        data = []
        for values in worker:
            data.append(values[4])
        workerData = {
            "label": worker[0][1],
            "backgroundColor": COLORS[index],
            "borderColor": COLORS[index],
            "fill": False,
            "tension": 0,
            "borderWidth": 1.3,
            "data": data,
        }
        datasets.append(workerData)

    data = {"labels": labels, "datasets": datasets}
    return data


@app.route("/updateshareschart", methods=["POST"])
def updateSharesChart():
    last24hData = getLast24hData()
    labels = []
    for label in last24hData[0]:
        labels.append(label[0])

    datasets = []
    for index, worker in enumerate(last24hData):
        data = []
        for values in worker:
            data.append(values[5])
        workerData = {
            "label": worker[0][1],
            "backgroundColor": COLORS[index],
            "borderColor": COLORS[index],
            "fill": False,
            "tension": 0,
            "borderWidth": 1.3,
            "data": data,
        }
        datasets.append(workerData)

    data = {"labels": labels, "datasets": datasets}
    return data


@app.route("/updatepowerchart", methods=["POST"])
def updatePowerChart():
    last24hData = getLast24hData()
    labels = []
    for label in last24hData[0]:
        labels.append(label[0])

    datasets = []
    for index, worker in enumerate(last24hData):
        data = []
        for values in worker:
            data.append(values[8])
        workerData = {
            "label": worker[0][1],
            "backgroundColor": COLORS[index],
            "borderColor": COLORS[index],
            "fill": False,
            "tension": 0,
            "borderWidth": 1.3,
            "data": data,
        }
        datasets.append(workerData)

    data = {"labels": labels, "datasets": datasets}
    return data


@app.route("/updatetemperaturechart", methods=["POST"])
def updateTemperatureChart():
    last24hData = getLast24hData()
    labels = []
    for label in last24hData[0]:
        labels.append(label[0])

    datasets = []
    for index, worker in enumerate(last24hData):
        data = []
        for values in worker:
            data.append(values[6])
        workerData = {
            "label": worker[0][1],
            "backgroundColor": COLORS[index],
            "borderColor": COLORS[index],
            "fill": False,
            "tension": 0,
            "borderWidth": 1.3,
            "data": data,
        }
        datasets.append(workerData)

    data = {"labels": labels, "datasets": datasets}
    return data


@app.route("/updateworkdonechart", methods=["POST"])
def updateWorkDoneChart():
    workDone = getWorkDone()

    colors = []
    for i, _ in enumerate(workDone):
        colors.append(COLORS[i])

    data = {
        "labels": list(workDone.keys()),
        "datasets": [
            {
                "label": "Work Done",
                "data": list(workDone.values()),
                "backgroundColor": colors,
                "borderColor": colors,
            }
        ],
    }
    return data