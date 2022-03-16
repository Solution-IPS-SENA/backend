from ast import Str
from time import strftime
from marshmallow import Schema, fields
from datetime import datetime as dt

data = dict(time="2020-03-23")

class TimeSchema(Schema):
    time = fields.AwareDateTime(strftime("%Y-%m-%d"))

obje = TimeSchema()
print(obje.validate(data))