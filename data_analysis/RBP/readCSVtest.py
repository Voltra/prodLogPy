#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../../exos/LG/")


import csv
from Array import Array
from ftfy import fix_text


"""
@:param path : The path of the csv file to turn into an array
@:param sep : The separator to use for spliting the csv row data
@:return : Return an array of values
"""
def printCsvFile(path, sep=None):
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile) if sep is None else csv.reader(csvFile, delimiter=sep)
        Array([elem for elem in reader])\
        .map(lambda elem : Array(elem).map(fix_text).toArray())        \
        .forEach(print)
    #
#
"""
@:param path : The path to the csv file to turn into a dictionnary
@:param sep : The separator to use for spliting the csv row data
@:return : Return a dictionnary of 'dict[key] = value' with key being the name of the row
"""
def getCsvAsDict(path, sep=None):
    csvFile = open(path, "r")
    return csv.DictReader(csvFile) if sep is None else csv.DictReader(csvFile, delimiter=sep)
#

if __name__ == "__main__":
    rscPath = "../../exos/rsc"
    csvPath = rscPath + "/data/csv"
    with open(csvPath + "/activites.csv", "rb") as csvFile :
        reader = csv.reader(csvFile)
        data = Array(list(reader))
        data.forEach(print)
    #
#