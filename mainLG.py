#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("data_analysis/LG/")
sys.path.append("exos/LG/")

from readCSVtest import printCsvFile, getCsvAsDict
from Array import Array

rscPath = "exos/rsc/data/"
csvPath = rscPath + "/csv"
csvFile = lambda x : csvPath + "/" + x

dict = list( getCsvAsDict( csvFile("equipements.csv"), ";" ) )
for row in dict:
    print("Amount of cols: " + str(len(row)))
    print("Columns: " + str(list(row.keys())))
    break