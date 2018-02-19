#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.apimodels.Activite import Activite
from app.sql.connection import DBConnection
import sqlite3


class ActiviteApiController(ApiController):
    def __init__(self): #, connection
        super().__init__(Activite(connection=DBConnection.get()))
    #
#

class ActiviteApiControllerRoot(ApiControllerRoot):
    def __init__(self): #, connection
        super().__init__(Activite(connection=DBConnection.get()))
    #
#