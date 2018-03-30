#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

from app.controllers.Controller import Controller
from app.models.Activite import Activite
from app.sql.connection import DBConnection
from flask_classful import FlaskView, route


class ActiviteController(Controller, FlaskView):
    def __init__(self):
        Controller.__init__(self, Activite(DBConnection.get()), "/activites")
    #

    @route("/codePostal/<string:zip>") #TODO: See if it works, if it doesn't fix it
    def zipCode(self, zip):
        print(zip)
        res = self.model.getForZip(zip)
        print(zip)
        return res
    #

    def inseeCode(self, insee):
        return self.model.getForInsee(insee)
    #
#