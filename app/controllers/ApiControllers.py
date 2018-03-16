#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse
from app.apimodels.ApiModel import ApiModel

"""
A class that manage the controller and allow to set a Model.
"""
class ApiController(Resource):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("limit", type=int, location="args", default=ApiModel.LIMIT, help="Limite en nombre")
        self.parser.add_argument("skip", type=int, location="args", default=0, help="Offset de recherche")
    #

    """
    Get all the values from the id in input.
    """
    def get(self, _id):
        args = self.parser.parse_args()
        limit = args["limit"]
        skip = args["skip"]
        return self.model.get(_id, limit, skip)
    #
#
"""
A class to load all the value of the model attach to the specified ApiController.
"""
class ApiControllerRoot(ApiController):
    def get(self):
        args = self.parser.parse_args()
        limit = args["limit"]
        skip = args["skip"]
        print(limit, skip, sep=" ")

        return self.model.getAll(limit, skip)
    #
#