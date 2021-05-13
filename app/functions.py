import os, json
import pandas as pd
from datetime import datetime


def getWorkersState():
    PATH = r"./data/json/workers/"
    workersState = []
    for file in os.listdir(PATH):
        while True:
            try:
                workersState.append(
                    json.load(
                        open(
                            f"{PATH}{file}",
                        )
                    )
                )
                break
            except:
                pass
    return workersState


def getAllWorkersData():
    PATH = r"./data/csv/workers/"
    allWorkersData = []
    for file in os.listdir(PATH):
        allWorkersData.append(pd.read_csv(f"{PATH}/{file}"))
    return allWorkersData


def getLast24hData():
    last24hData = []
    for worker in getAllWorkersData():
        workerData = []
        for row in worker[-1441:].values.tolist():
            if datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").minute % 5 == 0:
                workerData.append(row)
        last24hData.append(workerData)
    return last24hData


def getEarningsData():
    PATH = r"./data/csv/balance/balance.csv"
    data = pd.read_csv(PATH)
    return data.values.tolist()


def getWorkDone():
    workDone = {}
    for worker in getAllWorkersData():
        cont = 0
        for row in worker.values.tolist():
            if row[8] != 0:
                cont += 1
        workDone[worker["worker"][0]] = cont
    return workDone

def getPowerMedian():
    powerMedian = {}
    for worker in getAllWorkersData():
        cont = []
        for row in worker.values.tolist():
            if row[8] != 0:
                cont.append(row[8])
        powerMedian[worker["worker"][0]] = sum(cont)/len(cont)
    return powerMedian

def getHashrateMedian():
    hashrateMedian = {}
    for worker in getAllWorkersData():
        cont = []
        for row in worker.values.tolist():
            if row[8] != 0:
                cont.append(row[4])
        hashrateMedian[worker["worker"][0]] = sum(cont)/len(cont)
    return hashrateMedian