#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("data_analysis/LG/")
sys.path.append("exos/LG")

from writeCsvToSqlite import createTableFromData
import sqlite3

rscPath = "exos/rsc/data/"
csvPath = rscPath + "/csv"
csvFile = lambda x: csvPath + "/" + x

connection = sqlite3.connect("database_LG.db")
cursor = connection.cursor()
createTableFromData(tableName="activites", cursor=cursor, csvPath=csvFile("activites.csv"))
connection.commit()
cursor.close()