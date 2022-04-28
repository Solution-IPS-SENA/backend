from datetime import datetime
from src.config import APP

def time():
    return datetime.now().strftime(APP.DATETIME_FORMAT)
