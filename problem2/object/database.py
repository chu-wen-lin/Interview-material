# TODO: connect MongoDB
import os
from pymongo import MongoClient


def get_db():
    host = os.getenv("db_host")
    port = int(os.getenv("db_port"))
    client = MongoClient(host, port)
    db = client['Rent_591']
    collection = db['Taipei_Metropolitan_Area']
    return collection
