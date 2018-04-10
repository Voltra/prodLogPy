#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

from app.controllers.Controller import Controller
from app.models.Activite import Activite
from app.sql.connection import DBConnection
from flask_classful import FlaskView, route

"""
A controller class, contain method to access to the routes we've defined
"""
class ActiviteController(Controller, FlaskView):
    def __init__(self):
        Controller.__init__(self, Activite(DBConnection.get()), "/activites")
    #

    """
    The route we're using to pass argument from the view to the model in order to search using the postal code
    @:param zip - The postal code we're searching for
    """
    @route("/codePostal/<string:zip>") #TODO: See if it works, if it doesn't fix it
    def zipCode(self, zip):
        print(zip)
        res = self.model.getForZip(zip)
        print(zip)
        return res
    #

    """
    The route we're using to pass argument from the view to the model in order to search using the commune name
    @:param commune - The commune name we're searching for
    """
    @route("/commune/<string:commune>")
    def comLib(self, commune):
        print(commune)
        res = self.model.getForComLib(commune)
        print(res)
        return res
    #

    """
    The route we're using to pass argument from the view to the model in order to search using the activite name
    @:param activite - The activite name we're searching for
    """
    @route('/activites/<string:activite>')
    def actLib(self, activite):
        print(activite)
        res = self.model.getForActLib(activite)
        print(res)
        return res

    #
    """
    The route we're using to pass argument from the view to the model in order to search using the insee code
    @:param activite - The activite name we're searching for    
    """
    @route("/insee/<string:insee>")
    def inseeCode(self, insee):
        return self.model.getForInsee(insee)
    #
#
