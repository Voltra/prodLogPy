#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

class Installation(ApiModel):
    def __init__(self, connection):
        super().__init__(idCol="Numéro de l'installation", tableName="installations", connection=connection)
    #
#