#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import Resource

class ApiController(Resource):
    def __init__(self, model):
        super().__init__()
        self.model = model
    #

    def get(self, _id):
        return self.model.get(_id)
    #
#

class ApiControllerRoot(ApiController):
    def get(self):
        return self.model.getAll()
    #
#