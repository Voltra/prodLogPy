#!/usr/bin/python3
# -*- coding: utf-8 -*-
from app.models.Model import Model

"""
A class that allows to tap into the "activites" table
"""
class Installation(Model):
    def __init__(self, cursor):
        super().__init__("installations", cursor)
    #
#