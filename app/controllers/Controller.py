#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Base class for all "classic" controllers
"""
class Controller:
    """
    Initialize the Controller with a Model
    @:param model being an instance of models.Model
    @:param name being the name to use for routes building
    """
    def __init__(self, model, name):
        self.model = model
        self.name = name
    #

    """
    Generates the complete URI from the base URI of the Controller
    @:param ext being the extra URI to add to the base URI
    @:returns the crafted URI
    """
    def routeUri(self, ext=""):
        return self.name + ext;
    #
#