
# coding: utf-8
# Importacion de archivos x.geojson
import json
import pprint
from pymongo import MongoClient
client = MongoClient()
db= client.Peru
dbp = db.rios
data = open("Rios84.geojson")
x = json.load(data)
dbp.insert_many(x["features"])
#dbp.find_one() Look for one document
#dbp.drop() Delete your collection
