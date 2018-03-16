#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Installation import Installation
from app.sql.connection import DBConnection

"""
A class that create a controller for the "Installation" table.
"""
class InstallationApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Installation(connection=DBConnection.get()))
    #
#

"""
A class that create a controller for the "Installation" table and get all the values (do not mistake for InstallationApiController).
"""
class InstallationApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Installation(connection=DBConnection.get()))
    #
#