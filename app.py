'''
Created on 

Course work: 

@author: Elakia VM, Nagul

Source:
    
'''
from gc import collect
from multiprocessing import connection
import pymongo
import os
from dotenv import load_dotenv
import csv
import json

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

print(MONGO_URI)

client = pymongo.MongoClient(MONGO_URI)

client.list_database_names()

database_name   = "housilon_dev"
housilon_dev      = client[database_name]
collection_name = "hn_house_sample"
collection      = housilon_dev[collection_name]

file_path =  os.environ.get("FILE_NAME")

print(file_path)

FILEPATH = 'housilon-sample.json'

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

def csv_dict_list():
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open("/home/elakia/tact/data-to-mongodb/100_rows.csv", 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    #print(dict_list)
    return dict_list

def get_all_data():

    data = get_json_data() 

    # print(data)
    return data
    

def insert_one(document):
    collection.insert_one(document)
    return "successful inserted"

def insert_many(result):

    collection.insert_many(result)
    print("inserted")
    return "successful inserted many"

def query_one(query):
    print(collection.find_one(query))
    pass
def query_many(query_items):

    result = collection.find(query_items)
    for i in result:
        print(i)

    result = collection.find({}).limit(2)
    for i in result:
        print(1)

    pass

def query_particular(query_reg):

    print(collection.find_one(query_reg))

    pass
def update(query_update_reg,new_data):
    present_data=collection.find_one(query_update_reg)
    collection.update_one(present_data,new_data)
    print("successfully updated ")
    pass

def delete_one(query_delete_reg):

    collection.delete_one(query_delete_reg)
    print("successfully deleted ")
    pass

def delete_many(query_delete_items):

    collection.delete_many(query_delete_items)
    print("successfully deleted many")
    pass

# collection.drop()
# print("drop table")

def startpy():

    data = csv_dict_list()
    store_json_data(data)
    result = get_all_data()

    insert_many(result)

    # document = {
    #     "Name"  : "Raji",
    #     "Reg_No": 1234,
    #     "Branch": "IT"
    # }


    # insert_one(document)

    # items = [{
    #     "Name"  : "Ram",
    #     "Reg_No": 6234,
    #     "Branch": "CSE"
    # },
    # {
    #     "Name"  : "latha",
    #     "Reg_No": 7892,
    #     "Branch": "ECE"
    # },
    # {
    #     "Name"  : "Sai",
    #     "Reg_No": 4534,
    #     "Branch": "EEE"
    # }]

    # insert_many(items)

    # query = {
    #     "Name" : "Raji"
    # }

    # query_one(query)

    # query_items ={
    #     "Branch" : "ECE"
    # }

    # query_many(query_items)

    # query_reg={
    #     "Reg_No":{"$eq":1234}
    #     }

    # query_particular(query_reg)

    # query_update_reg={"Reg_No":{"$eq":1234}}
    # new_data={'$set':{"Name":'Ramesh'}}
    # update(query_update_reg,new_data)

    # query_delete_reg={"Reg_No":1234}
    # delete_one(query_delete_reg)

    # query_delete_items = {
    #     "Branch" : "ECE"
    # }
    # delete_many(query_delete_items)

startpy()