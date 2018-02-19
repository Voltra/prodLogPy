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

    def __init__(self, idCol, tableName, connection):
        super().__init__(tableName, connection)
        self.id = idCol
    #

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