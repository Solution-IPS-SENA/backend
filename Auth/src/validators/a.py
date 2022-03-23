from marshmallow import Schema, fields, validate
from datetime import datetime as dt
timee = dt.now()
data = dict(time=str(timee))
print(data)
class TimeSchema(Schema):
    time = fields.DateTime(required=True)

obje = TimeSchema()
print(obje.validate(data))