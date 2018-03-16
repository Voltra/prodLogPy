#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

"""
The ApiModel for the 'activites' table, using the 'ActCode' column as the ID column
"""
class Activite(ApiModel):
    """
    Instantiate a Activite object
    @:param connection being a SQLite3 DB connection
    """
    def __init__(self, connection):
        super().__init__(idCol="ActCode", tableName="activites", connection=connection)
    #
#