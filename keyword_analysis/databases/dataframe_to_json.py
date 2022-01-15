from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io
import json
from bson.json_util import dumps
# import MyJSON



class MySON:
    def __init__(self):
        pass
        # self.mylist = mylist
        # self.my_json = json.dumps(self.mylist)
    def set_dataframe(self, path):
        self.path = path
        self.df = pd.read_csv(self.path, encoding="utf-8-sig")
        self.df.fillna(0, inplace=True)
    def set_json_path(self, json_path):
        self.json_path = json_path
    def to_json(self, orient='records'):
        self.path_or_buf = self.json_path
        self.df.to_json(self.path_or_buf, orient)
    def to_mongodb(self, db_name, col_name, client="mongodb://localhost:27017/"):
        self.myclient = MongoClient(client) 
        self.db = self.myclient[db_name]
        self.col = self.db[col_name]
        with open(self.path_or_buf) as f:
            self.json_object = json.load(f)
        if isinstance(self.json_object, list):
            self.col.insert_many(self.json_object)  
        else:
            self.col.insert_one(self.json_object)
    def print_sample_df(self, row=20):
        print(self.df.head(row))
    def print_sample_json(self):
        pass
    # def save_as_json_file(self, dest):
    #     with open(dest, 'w') as f:
    #         json.dump(self.mylist, f, indent=2) 
    # def retrieve_json(self, path):        
    #     with open(path, 'r') as f:
    #         mylist = json.load(f)
    #     return mylist
    # def print_json(self):
    #     print(self.my_json)
    # def print_list(self, n=20):
    #     print(self.mylist[:n])



if __name__ == '__main__':
    csv_path = r"./canned_coffee_5star_processed.csv"
    m = MySON()
    m.set_dataframe(csv_path)
    json_path = r'./canned_coffee_5star_processed.json'
    m.set_json_path(json_path)
    m.to_json()
    db_name = 'canned_coffee'
    col_name = 'starbucks_frappuccino'
    m.to_mongodb(db_name=db_name, col_name=col_name)
    # df = pd.read_csv(r".\canned_coffee_5star_processed.csv", encoding="utf-8-sig", delimiter=',', thousands=r',', dtype=None, chunksize=None)
    # print(df.head())


    # records = json.loads(df.T.to_json()).values()
    # print(json.dumps(list(records), indent=2))


    # client = MongoClient()
    # db = client["canned_coffee"]
    # col = db["canned_coffee"]
    # # x = db.collection.insert_one(df.to_dict('records'))
    # # print(x.title[:10])
    # x = col.insert_many(records) # x = doc object?


    # print('\n--- INSERTED IDS ---')
    # print(x.inserted_ids)


    # print('\n--- FIRST DOCUMENT')
    # doc = col.find_one()
    # print(doc)


    # print('\n--- FIRST 5 DOCUMENTS')
    # for doc in col.find().limit(5):
    #     print(doc)
        
        
    # print('\n--- FIRST 5 TITLES')
    # for doc in col.find().limit(5):
    #     print(doc["title"])
        
        
    # print('\n--- TO JSON')    
    # with open('canned_coffee.json', 'w') as f:
    #     cursor = col.find({})
    #     json.dump(json.loads(dumps(cursor)), f)    