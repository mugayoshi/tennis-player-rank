import pymongo
from dotenv import load_dotenv
import os

def get_db(name='players'):
    load_dotenv()

    uri = os.environ['MONGODB_URI']
    client = pymongo.MongoClient(uri)
    return client.get_database(name)