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
from csv import DictReader
import json
import pprint

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)

# print(client.list_database_names())

database_name                   = "housilon_dev"
housilon_dev                    = client[database_name]
collection_hn_listing           = "hn_listing"
collection                      = housilon_dev[collection_hn_listing]
collection_hn_house_detail      = "hn_house_detail"
collection_house_detail         = housilon_dev[collection_hn_house_detail]
collection_hn_property_type     = "hn_property_type"
collection_property_type        = housilon_dev[collection_hn_property_type]
collection_hn_room              = "hn_room"
collection_room                 = housilon_dev[collection_hn_room]
collection_hn_house_sample      = "hn_house_sample"
collection_house_sample         = housilon_dev[collection_hn_house_sample]

FILE_PATH = "/Users/tactlabs/kaipulla_space/tact/data-to-mongodb/abc.csv"  #os.environ.get("FILE_PATH")

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
    with open(FILE_PATH,'r') as file:
        reader = DictReader(file)
        dict_list = []
        for line in reader:
            dict_list.append(line)
        return dict_list

def get_all_data():

    data = get_json_data() 

    # print(data)
    return data
    
def insert_one(hn):
    try:
        collection_house_sample.insert_one(hn)
        return "successful inserted"

    except Exception as e:
        print('Error : ', e)
    
    
# def insert_many():
#     with open("/home/elakia/tact/data-to-mongodb/housilon-sample.json") as file:
#     #     file_data = json.load(file)

#     # for c_index in data:

#     #     insert_one()

#     #     print(f'{c_index} Added: ', current_city, current_state)
#     pass

def query_one(result):
    print(collection.find_one(result))
    print("got the items")
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

def json_variable_getting(hn):
    if ( hn["house_house_id"] == "1"):

        result= {
            "house_id" : 1
        }  

        print(collection_house_detail.find_one(result))

        print("json_variable_getting | house_id : 1")

        new_data={ '$set' : {
            "end_date"          : hn["listings_0_end_date"],
        	"event"             : hn["listings_0_event"],
        	"house_id"          : hn["house_house_id"],
        	"listing_board_id"  : hn["listings_0_listing_board_id"],
        	"sold_price"        : hn["sold_price"],
        	"start_date"        : hn["listings_0_start_date"],
        	"update_at"         : hn["listings_0_update_at"],

        }	
        }

        present_data=collection.find_one(result)
        collection.update_one(present_data,new_data)
        print("successfully updated ")


        new_data_house_detail={
            '$set' : {
                "bathrooms"             : hn["house_details_partial_bathrooms"],
                "bedrooms"              : hn["house_details_bedrooms"],
                "cooling"               : hn["house_details_cooling"],
                "electricity"           : hn["house_details_electricity"],   
                "garage"                : hn["house_details_garage"],
                    "garage_type"           : hn["house_details_garage_type"],
                "gas"                   : hn["house_details_gas"],
                "heating_fuel"          : hn["house_details_heating_fuel"],
                "heating_type"          : hn["house_details_heating_type"],
                "house_id"              : hn["house_house_id"],
                "kitchens"              : hn["house_details_kitchens"],
                "parking_places"        : hn["house_details_parking_places"],
                "rooms"                 : hn["house_details_rooms"],
                "total_parking_space"   : hn["house_details_total_parking_space"],
                "water"                 : hn["house_details_water"]
            }
        }

        present_data=collection.find_one(result)
        collection_house_detail.update_one(present_data,new_data_house_detail)
        print("successfully updated ")

        new_data_hn_room={
            '$set' :{
                "house_id"      : hn["house_house_id"],
                "level"         : hn["rooms_0_level"],
                "type"          : hn["house_property_type"]
            }
        }
        present_data=collection.find_one(result)
        collection_room.update_one(present_data,new_data_hn_room)
        print("successfully updated ")


        new_data_property_type={
            '$set' :{
                "property_type"     : hn["house_property_type"]
            }
        }
                
        present_data=collection.find_one(result)
        collection_property_type.update_one(present_data,new_data_property_type)
        print("successfully updated ")

    return

# def get_single_data(house_id):

#     data = get_json_data() 

#     # if( house_id in data["house_house_id"]):
#     pprint(data)

#     # print(data)
#     return None



def startpy():

    data = csv_dict_list()
    for i in data :
        print(insert_one(i))
        
    # store_json_data(data)
    # for i in range(1,100):
    #     house_id = str(i)
        # print(type(house_id))
        # get_single_data(house_id)
  
    # json_variable_getting(hn)


    # result = get_all_data()

    # insert_many()

    # document = {
    #     "Name"  : "Raji",
    #     "Reg_No": 1234,
    #     "Branch": "IT"
    # }

    # hn = get_all_data()
    # insert_one(hn)

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