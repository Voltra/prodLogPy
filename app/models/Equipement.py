#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.models.Model import Model

"""
A class that allows to tap into the "equipements" table
"""
class Equipement(Model):
    def __init__(self, cursor):
        super().__init__("equipements", cursor)
    #
#