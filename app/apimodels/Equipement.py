#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

"""
The ApiModel for the 'equipements' table, using the 'EquipementId' column as the ID column
"""
class Equipement(ApiModel):
    """
    Instantiate a Equipement object
    @:param connection being a SQLite3 DB connection
    """
    def __init__(self, connection):
        super().__init__(idCol="EquipementId", tableName="equipements", connection=connection)
    #
#