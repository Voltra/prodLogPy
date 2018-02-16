#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Model:
    """
    @:param connection being a sqlite3 connection
    """
    def __init__(self, connection):
        self.co = connection
        self.cursor = self.co.cursor()
    #
#