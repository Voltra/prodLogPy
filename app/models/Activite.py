#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
from flask import jsonify

from app.models.Model import Model
from app.sql.connection import DBConnection
from app.sql.installationsParCodeInsee import installationsParCodeInsee
from app.sql.installationsParCodePostal import installationsParCodePostal
from app.sql.installationsParCommune import installationsParCommune
<<<<<<< HEAD
from app.sql.installationsParActivite import installationsParActivite
=======
>>>>>>> d90e891bf9d953f2f25ee77d8a2a09976ce310da

"""
A class that allows to tap into the "activites" table
"""
class Activite(Model):
    def __init__(self, cursor):
        super().__init__("activites", cursor)
    #

    """
    Method that make a call to InstallationParCodeInsee passing argument, in order to get all the information from the data base
    @:param self - it's the context
    @:param - insee - Insee number we're passing as an argument for the sql search 
    """
    def getForInsee(self, insee):
        # self.cursor.execute(installationsParCodeInsee(), insee)
        # return self.cursor.fetchall()

        co = DBConnection.factory()()
        # co = sqlite3.Connection(DBConnection.location)
        cursor = co.cursor()
        cursor.execute(installationsParCodeInsee(), {"insee": insee})
        try:
            return jsonify(cursor.fetchall())
        except sqlite3.Warning as e:
            return e, 500
    #

    """
    Method that make a call to InstallationParCodeInsee passing argument, in order to get all the information from the data base
    @:param self - it's the context
    @:param - zipcode - Postal code number we're passing as an argument for the sql search 
    """
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

    """
    Method that make a call to InstallationParCodeInsee passing argument, in order to get all the information from the data base
    @:param self - it's the context
    @:param - comLib - the name of the commune we're passing as an argument to the sql search 
    """
    def getForComLib(self, comlib):
        co = DBConnection.factory()()

        cursor = co.cursor()
        cursor.execute(installationsParCommune(), {"commune": comlib})
        try:
            return jsonify(cursor.fetchall())
        except sqlite3.Warning as e:
            return e, 500
    #

<<<<<<< HEAD
    def getForActLib(self, actlib):
        co = DBConnection.factory()()

        cursor = co.cursor()
        cursor.execute(installationsParActivite(), {"activite": actlib})
=======
    """
    Method that make a call to InstallationParCodeInsee passing argument, in order to get all the information from the data base
    @:param self - it's the context
    @:param - comLib - the name of the commune we're passing as an argument to the sql search 
    """
    def getForComLib(self, comblib):
        co = DBConnection.factory()()

        cursor = co.cursor()
        cursor.execute(installationsParCommune(), {"commune": comblib})
>>>>>>> d90e891bf9d953f2f25ee77d8a2a09976ce310da
        try:
            return jsonify(cursor.fetchall())
        except sqlite3.Warning as e:
            return e, 500
    #
#