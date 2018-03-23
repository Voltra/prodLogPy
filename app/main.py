#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from sqlite3 import Connection as SQLiteConnection

from app.controllers.ActiviteApiControllers import ActiviteApiController, ActiviteApiControllerRoot
from app.controllers.ApiControllers import ApiController, ApiControllerRoot
from app.controllers.EquipementApiControllers import EquipementApiController, EquipementApiControllerRoot
from app.controllers.InstallationApiControllers import InstallationApiController, InstallationApiControllerRoot
from app.sql.connection import DBConnection

app = Flask(__name__)
api = Api(app)

DATA = {
    "a": {"key": "value"},
    "b": {"key": "value"},
    "c": {"key": "value"},
}

parser = reqparse.RequestParser()
#parser.add_argument("key")

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

"""
The home route
"""
@app.route("/", endpoint="home")
def test():
    return jsonify(DATA)

"""
Just a test route
"""
@app.route("/test")
def test2():
    return render_template("test.twig", name=120)

def makeApiUrl(uri):
    return "/api" + uri
#

"""
Route who's purpose is to allow access to specific data using an id, 
like the one use for the equipement, like the one use for the equipement
"""
api.add_resource(Data, makeApiUrl("/data/<_id>"))

connection = SQLiteConnection("../database_LG.db")
cursor = connection.cursor()
cursor.execute("SELECT  name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

"""
A route that allows us to get information from the activites table using an id present in the given table
"""
api.add_resource(ActiviteApiController, makeApiUrl("/activites/<string:_id>"), endpoint="activite")

"""
A route that allows us to get all the data from the activites database
"""
api.add_resource(ActiviteApiControllerRoot, makeApiUrl("/activites"), endpoint="activites")

"""
A route that allows us to get information from the equipements table, using an id present in the given table
"""
api.add_resource(EquipementApiController, makeApiUrl("/equipements/<string:_id>"), endpoint="equipement")

"""
A route that allows us to get all the data from the equipements database
"""
api.add_resource(EquipementApiControllerRoot, makeApiUrl("/equipements"), endpoint="equipements")

"""
A route that allows us to get information from the installation table, using an id present in the given table
"""
api.add_resource(InstallationApiController, makeApiUrl("/installations/<string:_id>"), endpoint="installation")

"""
A route that allows us to get all the data from the installations database
"""
api.add_resource(InstallationApiControllerRoot, makeApiUrl("/installations"), endpoint="installations")

"""
Part that actually runs the app an therefore launches the server
"""
if __name__ == "__main__":
    app.run(debug=True)