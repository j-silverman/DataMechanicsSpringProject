#import dml
import pymongo
import os 
from dotenv import load_dotenv
load_dotenv()

def get_repo():
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

    client = pymongo.MongoClient(MONGO_HOST, username=MONGO_USER,
                      password=MONGO_PASSWORD)



    repo = client['jhs2018_rpm1995']
    #repo.authenticate('jhs2018_rpm1995', 'jhs2018_rpm1995')

    return repo

r = get_repo()
