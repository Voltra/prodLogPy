#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../exos/LG/")

from readCSVtest import printCsvFile, getCsvAsDict

if __name__ == "__main__":
    rscPath = "exos/rsc/data/"
    csvPath = rscPath + "/csv"
    csvFile = lambda x: csvPath + "/" + x

    dict = list(getCsvAsDict(csvFile("equipements.csv"), ";"))
    for row in dict:
        print("Amount of cols: " + str(len(row)))
        print("Columns: " + str(list(row.keys())))
        break
    #
#