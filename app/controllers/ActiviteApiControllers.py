#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Activite import Activite
from app.sql.connection import DBConnection
import sqlite3

"""
A class that create a controller for the "Activities" table.
"""
class ActiviteApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Activite(connection=DBConnection.get()))
    #
#

"""
A class that create a controller for the "Activities" table and get all the values (do not mistake for ActiviteApiController).
"""
class ActiviteApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Activite(connection=DBConnection.get()))
    #
#