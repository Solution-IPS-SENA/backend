from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from redis import Redis

db: SQLAlchemy = SQLAlchemy()
rd: Redis = FlaskRedis(decode_responses=True)