#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Equipement import Equipement
from app.sql.connection import DBConnection

"""
A class that create a controller for the "Equipement" table.
"""
class EquipementApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Equipement(connection=DBConnection.get()))
    #
#

"""
A class that create a controller for the "Equipement" table and get all the values (do not mistake for EquipementApiController).
"""
class EquipementApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Equipement(connection=DBConnection.get()))
    #
#