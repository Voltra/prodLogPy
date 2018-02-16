#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Array import Array
from readCSVtest import getCsvAsDict
from ftfy import fix_text
import numbers

"""
Creates a SQLite3 table from a correct CSV file

@:param tableName being the desired table name in the database
@:param cursor being a sqlite3 cursor (will be used in order to perform database interaction)
@:param csvPath being the path to the CSV file that contains the initial data
@:param sep being the separator used in the CSV file (defaulted to ',')
@:raise AssertionError if the CSV file contains no initial data (whether or not it contains the headers)
"""
def createTableFromData(tableName, cursor, csvPath, sep=","):
    rows = list(getCsvAsDict(csvPath, sep))
    if len(rows) < 1 :
        raise AssertionError("The given CSV file should at least have 1 row of data in order to create the said table from existing data")
    keys = Array( list(rows[0].keys()) )


    fixUtf8IfString = lambda v : fix_text(v) if not isinstance(v, numbers.Number) else v

    strTableName = str(tableName)

    keysJoined = keys.map(fixUtf8IfString).map(lambda s : "`"+s+"`").join(", ")
    print(keysJoined)
    cursor.execute("DROP TABLE IF EXISTS " + strTableName)
    cursor.execute("CREATE TABLE IF NOT EXISTS " + strTableName + " (" + keysJoined + ")")

    parseBoolIfBool = lambda s : True if s == "Oui" else False if s == "Non" else s

    for row in rows:
        values = Array(list(row.values())).map(fixUtf8IfString).map(parseBoolIfBool).toArray()
        placeholders = keys.map(lambda x: "?").join(", ")
        cursor.execute("INSERT INTO " + strTableName + "(" + keysJoined + ") VALUES (" + placeholders + ")", values)
#