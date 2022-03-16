from os import getenv

class DB():
    HOST = getenv("DB_HOST")
    USER = getenv("DB_USER")
    PASS = getenv("DB_PASS")
    NAME = getenv("DB_NAME")
    PORT = int(getenv("DB_PORT"))