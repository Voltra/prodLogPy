#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

class Equipement(ApiModel):
    def __init__(self, connection):
        super().__init__(idCol="EquipementId", tableName="equipements", connection=connection)
    #
#