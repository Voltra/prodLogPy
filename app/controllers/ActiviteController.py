#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

from app.controllers.Controller import Controller
from app.models.Activite import Activite
from app.sql.connection import DBConnection
from flask_classful import FlaskView, route


class ActiviteController(Controller, FlaskView):
    def __init__(self):
        co = sqlite3.Connection(DBConnection.location)
        co.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
        Controller.__init__(self, Activite(co), "/activites")
    #

    @route("/codePostal/<string:zip>/") #TODO: See if it works, if it doesn't fix it
    def zipCode(self, zip):
        return self.model.getForZip(zip)
    #

    def inseeCode(self, insee):
        return self.model.getForInsee(insee)
    #
#