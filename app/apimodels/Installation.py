#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

"""
The ApiModel for the 'installations' table, using the 'Numéro de l'installation' column as the ID column
"""
class Installation(ApiModel):
    """
    Instantiate a Installation object
    @:param connection being a SQLite3 DB connection
    """
    def __init__(self, connection):
        super().__init__(idCol="Numéro de l'installation", tableName="installations", connection=connection)
    #
#