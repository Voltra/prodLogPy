#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Equipement import Equipement
from app.sql.connection import DBConnection


class EquipementApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Equipement(connection=DBConnection.get()))
    #
#

class EquipementApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Equipement(connection=DBConnection.get()))
    #
#