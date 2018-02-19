#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.utils.Array import Array

"""
An abstract class that allows to tap into a SQLite table
"""
class Model:
    """
    Constructor
    @:param tableName being the name of the table associated to this Model (in your database)
    @:param connection being a sqlite3 connection
    """
    def __init__(self, tableName, connection):
        self.table = tableName
        self.co = connection
        self.cursor = self.co.cursor()
    #

    """
    Insert a tuple of value in the table associated to this Model
    @:param valuesOrderedDic being an ordered dictionnary (keys -> column name, values)
    @:returns self (for chaining purposes)
    """
    def insert(self, valuesOrderedDic):
        values = valuesOrderedDic.values()
        descriptor = Array(valuesOrderedDic.keys()).map(lambda s: "`{}`"%s).join(", ")
        valuesPrep = Array(values).map(lambda x : "?").join(", ")
        self.cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (self.table, descriptor, valuesPrep), values)
        return self
    #

    """
    Insert many tuples of value in the table associated to this Model
    @:param keys being an iterable containing the keys (in your database) in a given order
    @:param valuesArray being an iterable containing tuples of values (same order as for the keys)
    @:returns self (for chaining purposes)
    """
    def insertMany(self, keys, valuesArray):
        descriptor = Array(keys).map(lambda s: "`{}`"%s).join(", ")
        valuesPrep = Array(keys).map(lambda s: "?").join(", ")
        self.cursor.executemany("INSERT INTO %s (%s) VALUES (%s)" % (self.table, descriptor, valuesPrep), valuesArray)
        return self
    #

    """
    Commit changes
    @:returns self (for chaining purposes)
    """
    def commit(self):
        self.co.commit()
        return self
    #

    def __del__(self):
        self.co.close()
    #
#