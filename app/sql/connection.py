#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

import os

"""
Initialising the connection to database files
"""
class DBConnection:
    dirPath = os.path.dirname(os.path.realpath(__file__))
    location = dirPath + "/../../database_LG.db"

    @staticmethod
    def get():
        co = sqlite3.Connection(DBConnection.location)
        co.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
        return co
    #

    @staticmethod
    def factory():
        return DBConnection.get
    #
#