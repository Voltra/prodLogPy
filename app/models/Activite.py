#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.models.Model import Model
from app.sql.installationsParCodeInsee import installationsParCodeInsee

"""
A class that allows to tap into the "activites" table
"""
class Activite(Model):
    def __init__(self, cursor):
        super().__init__("activites", cursor)
    #

    def getForInsee(self, insee):
        self.cursor.execute(installationsParCodeInsee(), insee)
        return self.cursor.fetchall()
    #
#