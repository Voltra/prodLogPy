#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Installation import Installation
from app.sql.connection import DBConnection


class InstallationApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Installation(connection=DBConnection.get()))
    #
#

class InstallationApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Installation(connection=DBConnection.get()))
    #
#