from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io
import json
from bson.json_util import dumps
# import MySON







if __name__ == '__main__':
    df = pd.read_csv(r".\canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    print(df.head())


    records = json.loads(df.T.to_json()).values()
    print(json.dumps(list(records), indent=2))


    client = MongoClient()
    db = client["canned_coffee"]
    col = db["canned_coffee"]
    # x = db.collection.insert_one(df.to_dict('records'))
    # print(x.title[:10])
    x = col.insert_many(records) # x = doc object?


    print('\n--- INSERTED IDS ---')
    print(x.inserted_ids)


    print('\n--- FIRST DOCUMENT')
    doc = col.find_one()
    print(doc)


    print('\n--- FIRST 5 DOCUMENTS')
    for doc in col.find().limit(5):
        print(doc)
        
        
    print('\n--- FIRST 5 TITLES')
    for doc in col.find().limit(5):
        print(doc["title"])
        
        
    print('\n--- TO JSON')    
    with open('canned_coffee_5star_processed.json', 'w') as f:
        cursor = col.find({})
        json.dump(json.loads(dumps(cursor)), f)    