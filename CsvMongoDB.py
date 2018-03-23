
# coding: utf-8
# Importacion de archivos x
import pandas as pd
import pprint
from pymongo import MongoClient
import json

client = MongoClient()
db= client.Csv
dbd = db.data_4
data = pd.read_csv("DataPie.csv")
data_json = json.loads(data.to_json(orient='records'))
dbd.insert_many(data_json)





