#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../exos/LG/")


import csv
from Array import Array
from ftfy import fix_text

def printCsvFile(path, sep=None):
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile) if sep is None else csv.reader(csvFile, delimiter=sep)
        Array([elem for elem in reader])\
        .map(lambda elem : Array(elem).map(fix_text).toArray())        \
        .forEach(print)
    #
#

def getCsvAsDict(path, sep=None):
    csvFile = open(path, "r")
    return csv.DictReader(csvFile) if sep is None else csv.DictReader(csvFile, delimiter=sep)
#

if __name__ == "__main__":
    rscPath = "../../exos/rsc"
    csvPath = rscPath + "/csv"
    with open(csvPath + "/activites.csv", "rb") as csvFile :
        reader = csv.reader(csvFile)
        data = Array(reader)
        data.forEach(print)
    #
#