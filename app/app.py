#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

DATA = {
    "a": {"key": "value"},
    "b": {"key": "value"},
    "c": {"key": "value"},
}

parser = reqparse.RequestParser()
parser.add_argument("key")

def abortIfNotExists(_id):
    if _id not in DATA:
        abort(404, message="Object {} does not exists"%_id)
#

class Data(Resource):
    def get(self, _id):
        abortIfNotExists(_id)
        return DATA[_id]
    #
#

@app.route("/")
def test():
    return jsonify(DATA)

def makeApiUrl(uri):
    return "/api" + uri
#

api.add_resource(Data, makeApiUrl("/data/<_id>"))

if __name__ == "__main__":
    app.run(debug=True)