#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Resource

"""
A class that manage the controller and allow to set a Model.
"""
class ApiController(Resource):
    def __init__(self, model):
        super().__init__()
        self.model = model
    #

    """
    Get all the values from the id in input.
    """
    def get(self, _id):
        return self.model.get(_id)
    #
#
"""
A class to load all the value of the model attach to the specified ApiController.
"""
class ApiControllerRoot(ApiController):
    def get(self):
        return self.model.getAll()
    #
#