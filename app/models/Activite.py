#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
from flask import jsonify

from app.models.Model import Model
from app.sql.connection import DBConnection
from app.sql.installationsParCodeInsee import installationsParCodeInsee
from app.sql.installationsParCodePostal import installationsParCodePostal

"""
A class that allows to tap into the "activites" table
"""
class Activite(Model):
    def __init__(self, cursor):
        super().__init__("activites", cursor)
    #

    def getForInsee(self, insee):
        self.cursor.execute(installationsParCodeInsee(), insee)
        return self.cursor.fetchall()
    #

    def getForZip(self, zipcode):
        co = DBConnection.factory()()
        # co = sqlite3.Connection(DBConnection.location)
        cursor = co.cursor()
        cursor.execute(installationsParCodePostal(), {"zip": zipcode})
        try:
            return jsonify(cursor.fetchall())
        except sqlite3.Warning as e:
            return e, 500

    #
#