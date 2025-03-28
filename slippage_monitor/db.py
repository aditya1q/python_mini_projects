# db.py
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # Local MongoDB
    db = client['slippage_monitor']  # Database name
    return db

def init_db():
    db = get_db()
    # Create a collection (table equivalent) for trades if it doesn't exist
    trades = db['trades']
    return trades