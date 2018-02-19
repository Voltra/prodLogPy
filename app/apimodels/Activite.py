#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.apimodels.ApiModel import ApiModel

class Activite(ApiModel):
    def __init__(self, connection):
        super().__init__(idCol="ActCode", tableName="activites", connection=connection)
    #
#