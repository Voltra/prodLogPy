#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.models.Model import Model
from flask_restful import abort
import sqlite3

"""
A class that factorizes the behavior of models used for the API
"""
class ApiModel(Model):
    LIMIT = 20

    """
    Construct an ApiModel from meta data of a DB table
    @:param idCol being the column that serves as an ID
    @:param tableName being the name of the table bound to this ApiModel
    @:param connection being an SQLite3 DB connection
    """
    def __init__(self, idCol, tableName, connection):
        super().__init__(tableName, connection)
        self.id = idCol
    #


    """
    Determines whether or not there's an item that has the given id in th DB tabe
    @:param _id being the ID to test
    @:returns A response tuple (Boolean, Status), True if it exists, False otherwise ; a status 200 if everything went well, 400 if there were an error
    """
    def exists(self, _id):
        query = "SELECT * FROM `%s` WHERE `%s` like ? LIMIT 1" % (self.table, self.id)

        try:
            self.cursor.execute(query, (_id,))
        except sqlite3.Error as e:
            abort(400, message=e.args[0])
        except sqlite3.Warning as e:
            abort(400, message=e.args[0])

        length = len(self.cursor.fetchall())
        return length != 0, 200
    #

    """
    Retrieve the data associated to the given ID in the bound table
    @:param _id being the ID of the tuple to retrieve
    @:returns a response tuple (Json, Status), the data associated to the tuple ; 200 if there were no error, 400 if there were any
    """
    def get(self, _id):
        if not self.exists(_id):
            abort(404, message="No resource matching the given id")

        query = "SELECT * FROM `%s` WHERE `%s` like ? LIMIT %d" % (self.table, self.id, ApiModel.LIMIT)
        try:
            self.cursor.execute(query, (_id,))
        except sqlite3.Error as e:
            abort(400, message=e.args[0])
        except sqlite3.Warning as e:
            abort(400, message=e.args[0])

        return self.cursor.fetchall(), 200
    #

    """
    Retrieve "all" the data from the bound table (limited by a limit amount)
    @:returns a response tuple (Json, Status), the data associated to the tuple ; 200 if there were no error, 400 if there were any
    """
    def getAll(self):
        query = "SELECT * FROM %s LIMIT %d" % (self.table, ApiModel.LIMIT)

        try:
            self.cursor.execute(query)
        except sqlite3.DatabaseError as e:
            abort(400, message=e.args[0])
        except sqlite3.Warning as e:
            abort(400, message=e.args[0])

        return self.cursor.fetchall(), 200
    #


#