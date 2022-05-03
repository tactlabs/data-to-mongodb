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

database_name                   = "housilon_dev"
housilon_dev                    = client[database_name]
collection_hn_listing           = "hn_listing"
collection                      = housilon_dev[collection_hn_listing]
collection_hn_house_detail      = "hn_house_detail"
collection_house_detail         = housilon_dev[collection_hn_house_detail]
collection_hn_property_type     = "hn_property_type"
collection_property_type        = housilon_dev[collection_hn_property_type]
collection_hn_room              = "hn_room"
collection_room                 = housilon_dev["hn_room"]

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

        # new_data={ '$set' : {
        #     "end_date"          : hn["listings_0_end_date"],
        # 	"event"             : hn["listings_0_event"],
        # 	"house_id"          : hn["house_house_id"],
        # 	"listing_board_id"  : hn["listings_0_listing_board_id"],
        # 	"sold_price"        : hn["sold_price"],
        # 	"start_date"        : hn["listings_0_start_date"],
        # 	"update_at"         : hn["listings_0_update_at"],

        # }	
        # }

        # present_data=collection.find_one(result)
        # collection.update_one(present_data,new_data)
        # print("successfully updated ")


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


    pass

def startpy():

    # data = csv_dict_list()
    # store_json_data(data)
  
    hn = {
        "estimated_price": "",
        "house_address": "162 May Ave",
        "house_community": "North Richvale",
        "house_details_2_piece_bathrooms": "",
        "house_details_3_piece_bathrooms": "",
        "house_details_4_piece_bathrooms": "",
        "house_details_5_plus_piece_bathrooms": "",
        "house_details_appliances_excluded": "",
        "house_details_appliances_included": "",
        "house_details_appliances_remark": "",
        "house_details_basement_finish": "",
        "house_details_basement_finished": "",
        "house_details_basement_type": "Unfinished",
        "house_details_bathrooms": "1.0",
        "house_details_bathrooms_detail": "",
        "house_details_baths_on_level_basement": "",
        "house_details_baths_on_level_lower": "",
        "house_details_baths_on_level_main": "",
        "house_details_baths_on_level_second": "",
        "house_details_baths_on_level_third": "",
        "house_details_baths_on_level_upper": "",
        "house_details_bedrooms": "3",
        "house_details_bedrooms_above_ground": "",
        "house_details_bedrooms_below_ground": "",
        "house_details_beds_on_level_basement": "",
        "house_details_beds_on_level_lower": "",
        "house_details_beds_on_level_main": "",
        "house_details_beds_on_level_second": "",
        "house_details_beds_on_level_third": "",
        "house_details_beds_on_level_upper": "",
        "house_details_cable": "",
        "house_details_central_vac": "",
        "house_details_cooling": "",
        "house_details_docking": "",
        "house_details_docking_features": "",
        "house_details_electricity": "",
        "house_details_ensuite_bathrooms": "",
        "house_details_family_room": "Y",
        "house_details_feature": "",
        "house_details_features": "",
        "house_details_fireplace": "",
        "house_details_fireplace_total": "",
        "house_details_full_bathrooms": "",
        "house_details_garage": "",
        "house_details_garage_type": "Attached",
        "house_details_gas": "",
        "house_details_half_bathrooms": "",
        "house_details_heating": "",
        "house_details_heating_fuel": "Gas",
        "house_details_heating_secondary": "",
        "house_details_heating_type": "Forced Air",
        "house_details_hn_details_id": "1",
        "house_details_house_id": "1",
        "house_details_kitchens": "1.0",
        "house_details_kitchens_above_ground": "",
        "house_details_kitchens_below_ground": "",
        "house_details_kitchens_on_level_basement": "",
        "house_details_kitchens_on_level_lower": "",
        "house_details_kitchens_on_level_main": "",
        "house_details_kitchens_on_level_second": "",
        "house_details_kitchens_on_level_third": "",
        "house_details_laundries_on_level_basement": "",
        "house_details_laundries_on_level_lower": "",
        "house_details_laundries_on_level_main": "",
        "house_details_laundries_on_level_second": "",
        "house_details_laundries_on_level_third": "",
        "house_details_laundry": "",
        "house_details_laundry_facilities": "",
        "house_details_laundry_features": "",
        "house_details_parking_included": "",
        "house_details_parking_places": "6",
        "house_details_partial_bathrooms": "",
        "house_details_rooms": "5.0",
        "house_details_telephone": "",
        "house_details_total_parking": "",
        "house_details_total_parking_space": "",
        "house_details_water": "Municipal",
        "house_details_water_treatment": "",
        "house_fronting_on": "",
        "house_house_id": "1",
        "house_municipality": "Richmond Hill",
        "house_postal_code": "L4C3S6",
        "house_property_type": "Detached",
        "house_style": "Bungalow",
        "listings_0_end_date": "2022-02-04",
        "listings_0_event": "Sold",
        "listings_0_house_id": "1.0",
        "listings_0_listing_board_id": "N5483762",
        "listings_0_price": "2405000.0",
        "listings_0_start_date": "2022-01-28",
        "listings_0_update_at": "2022-02-08",
        "listings_10_end_date": "",
        "listings_10_event": "",
        "listings_10_house_id": "",
        "listings_10_listing_board_id": "",
        "listings_10_price": "",
        "listings_10_start_date": "",
        "listings_10_update_at": "",
        "listings_11_end_date": "",
        "listings_11_event": "",
        "listings_11_house_id": "",
        "listings_11_listing_board_id": "",
        "listings_11_price": "",
        "listings_11_start_date": "",
        "listings_11_update_at": "",
        "listings_12_end_date": "",
        "listings_12_event": "",
        "listings_12_house_id": "",
        "listings_12_listing_board_id": "",
        "listings_12_price": "",
        "listings_12_start_date": "",
        "listings_12_update_at": "",
        "listings_13_end_date": "",
        "listings_13_event": "",
        "listings_13_house_id": "",
        "listings_13_listing_board_id": "",
        "listings_13_price": "",
        "listings_13_start_date": "",
        "listings_13_update_at": "",
        "listings_14_end_date": "",
        "listings_14_event": "",
        "listings_14_house_id": "",
        "listings_14_listing_board_id": "",
        "listings_14_price": "",
        "listings_14_start_date": "",
        "listings_14_update_at": "",
        "listings_15_end_date": "",
        "listings_15_event": "",
        "listings_15_house_id": "",
        "listings_15_listing_board_id": "",
        "listings_15_price": "",
        "listings_15_start_date": "",
        "listings_15_update_at": "",
        "listings_16_end_date": "",
        "listings_16_event": "",
        "listings_16_house_id": "",
        "listings_16_listing_board_id": "",
        "listings_16_price": "",
        "listings_16_start_date": "",
        "listings_16_update_at": "",
        "listings_17_end_date": "",
        "listings_17_event": "",
        "listings_17_house_id": "",
        "listings_17_listing_board_id": "",
        "listings_17_price": "",
        "listings_17_start_date": "",
        "listings_17_update_at": "",
        "listings_18_end_date": "",
        "listings_18_event": "",
        "listings_18_house_id": "",
        "listings_18_listing_board_id": "",
        "listings_18_price": "",
        "listings_18_start_date": "",
        "listings_18_update_at": "",
        "listings_19_end_date": "",
        "listings_19_event": "",
        "listings_19_house_id": "",
        "listings_19_listing_board_id": "",
        "listings_19_price": "",
        "listings_19_start_date": "",
        "listings_19_update_at": "",
        "listings_1_end_date": "2021-11-16",
        "listings_1_event": "Terminated",
        "listings_1_house_id": "1.0",
        "listings_1_listing_board_id": "N5389291",
        "listings_1_price": "4188000.0",
        "listings_1_start_date": "2021-10-01",
        "listings_1_update_at": "2022-02-08",
        "listings_20_end_date": "",
        "listings_20_event": "",
        "listings_20_house_id": "",
        "listings_20_listing_board_id": "",
        "listings_20_price": "",
        "listings_20_start_date": "",
        "listings_20_update_at": "",
        "listings_21_end_date": "",
        "listings_21_event": "",
        "listings_21_house_id": "",
        "listings_21_listing_board_id": "",
        "listings_21_price": "",
        "listings_21_start_date": "",
        "listings_21_update_at": "",
        "listings_22_end_date": "",
        "listings_22_event": "",
        "listings_22_house_id": "",
        "listings_22_listing_board_id": "",
        "listings_22_price": "",
        "listings_22_start_date": "",
        "listings_22_update_at": "",
        "listings_23_end_date": "",
        "listings_23_event": "",
        "listings_23_house_id": "",
        "listings_23_listing_board_id": "",
        "listings_23_price": "",
        "listings_23_start_date": "",
        "listings_23_update_at": "",
        "listings_24_end_date": "",
        "listings_24_event": "",
        "listings_24_house_id": "",
        "listings_24_listing_board_id": "",
        "listings_24_price": "",
        "listings_24_start_date": "",
        "listings_24_update_at": "",
        "listings_25_end_date": "",
        "listings_25_event": "",
        "listings_25_house_id": "",
        "listings_25_listing_board_id": "",
        "listings_25_price": "",
        "listings_25_start_date": "",
        "listings_25_update_at": "",
        "listings_26_end_date": "",
        "listings_26_event": "",
        "listings_26_house_id": "",
        "listings_26_listing_board_id": "",
        "listings_26_price": "",
        "listings_26_start_date": "",
        "listings_26_update_at": "",
        "listings_27_end_date": "",
        "listings_27_event": "",
        "listings_27_house_id": "",
        "listings_27_listing_board_id": "",
        "listings_27_price": "",
        "listings_27_start_date": "",
        "listings_27_update_at": "",
        "listings_28_end_date": "",
        "listings_28_event": "",
        "listings_28_house_id": "",
        "listings_28_listing_board_id": "",
        "listings_28_price": "",
        "listings_28_start_date": "",
        "listings_28_update_at": "",
        "listings_29_end_date": "",
        "listings_29_event": "",
        "listings_29_house_id": "",
        "listings_29_listing_board_id": "",
        "listings_29_price": "",
        "listings_29_start_date": "",
        "listings_29_update_at": "",
        "listings_2_end_date": "2021-03-25",
        "listings_2_event": "Sold",
        "listings_2_house_id": "1.0",
        "listings_2_listing_board_id": "N5155757",
        "listings_2_price": "3425000.0",
        "listings_2_start_date": "2021-03-17",
        "listings_2_update_at": "2022-02-08",
        "listings_30_end_date": "",
        "listings_30_event": "",
        "listings_30_house_id": "",
        "listings_30_listing_board_id": "",
        "listings_30_price": "",
        "listings_30_start_date": "",
        "listings_30_update_at": "",
        "listings_31_end_date": "",
        "listings_31_event": "",
        "listings_31_house_id": "",
        "listings_31_listing_board_id": "",
        "listings_31_price": "",
        "listings_31_start_date": "",
        "listings_31_update_at": "",
        "listings_32_end_date": "",
        "listings_32_event": "",
        "listings_32_house_id": "",
        "listings_32_listing_board_id": "",
        "listings_32_price": "",
        "listings_32_start_date": "",
        "listings_32_update_at": "",
        "listings_33_end_date": "",
        "listings_33_event": "",
        "listings_33_house_id": "",
        "listings_33_listing_board_id": "",
        "listings_33_price": "",
        "listings_33_start_date": "",
        "listings_33_update_at": "",
        "listings_34_end_date": "",
        "listings_34_event": "",
        "listings_34_house_id": "",
        "listings_34_listing_board_id": "",
        "listings_34_price": "",
        "listings_34_start_date": "",
        "listings_34_update_at": "",
        "listings_35_end_date": "",
        "listings_35_event": "",
        "listings_35_house_id": "",
        "listings_35_listing_board_id": "",
        "listings_35_price": "",
        "listings_35_start_date": "",
        "listings_35_update_at": "",
        "listings_36_end_date": "",
        "listings_36_event": "",
        "listings_36_house_id": "",
        "listings_36_listing_board_id": "",
        "listings_36_price": "",
        "listings_36_start_date": "",
        "listings_36_update_at": "",
        "listings_37_end_date": "",
        "listings_37_event": "",
        "listings_37_house_id": "",
        "listings_37_listing_board_id": "",
        "listings_37_price": "",
        "listings_37_start_date": "",
        "listings_37_update_at": "",
        "listings_38_end_date": "",
        "listings_38_event": "",
        "listings_38_house_id": "",
        "listings_38_listing_board_id": "",
        "listings_38_price": "",
        "listings_38_start_date": "",
        "listings_38_update_at": "",
        "listings_39_end_date": "",
        "listings_39_event": "",
        "listings_39_house_id": "",
        "listings_39_listing_board_id": "",
        "listings_39_price": "",
        "listings_39_start_date": "",
        "listings_39_update_at": "",
        "listings_3_end_date": "",
        "listings_3_event": "",
        "listings_3_house_id": "",
        "listings_3_listing_board_id": "",
        "listings_3_price": "",
        "listings_3_start_date": "",
        "listings_3_update_at": "",
        "listings_40_end_date": "",
        "listings_40_event": "",
        "listings_40_house_id": "",
        "listings_40_listing_board_id": "",
        "listings_40_price": "",
        "listings_40_start_date": "",
        "listings_40_update_at": "",
        "listings_41_end_date": "",
        "listings_41_event": "",
        "listings_41_house_id": "",
        "listings_41_listing_board_id": "",
        "listings_41_price": "",
        "listings_41_start_date": "",
        "listings_41_update_at": "",
        "listings_42_end_date": "",
        "listings_42_event": "",
        "listings_42_house_id": "",
        "listings_42_listing_board_id": "",
        "listings_42_price": "",
        "listings_42_start_date": "",
        "listings_42_update_at": "",
        "listings_43_end_date": "",
        "listings_43_event": "",
        "listings_43_house_id": "",
        "listings_43_listing_board_id": "",
        "listings_43_price": "",
        "listings_43_start_date": "",
        "listings_43_update_at": "",
        "listings_44_end_date": "",
        "listings_44_event": "",
        "listings_44_house_id": "",
        "listings_44_listing_board_id": "",
        "listings_44_price": "",
        "listings_44_start_date": "",
        "listings_44_update_at": "",
        "listings_45_end_date": "",
        "listings_45_event": "",
        "listings_45_house_id": "",
        "listings_45_listing_board_id": "",
        "listings_45_price": "",
        "listings_45_start_date": "",
        "listings_45_update_at": "",
        "listings_46_end_date": "",
        "listings_46_event": "",
        "listings_46_house_id": "",
        "listings_46_listing_board_id": "",
        "listings_46_price": "",
        "listings_46_start_date": "",
        "listings_46_update_at": "",
        "listings_47_end_date": "",
        "listings_47_event": "",
        "listings_47_house_id": "",
        "listings_47_listing_board_id": "",
        "listings_47_price": "",
        "listings_47_start_date": "",
        "listings_47_update_at": "",
        "listings_48_end_date": "",
        "listings_48_event": "",
        "listings_48_house_id": "",
        "listings_48_listing_board_id": "",
        "listings_48_price": "",
        "listings_48_start_date": "",
        "listings_48_update_at": "",
        "listings_49_end_date": "",
        "listings_49_event": "",
        "listings_49_house_id": "",
        "listings_49_listing_board_id": "",
        "listings_49_price": "",
        "listings_49_start_date": "",
        "listings_49_update_at": "",
        "listings_4_end_date": "",
        "listings_4_event": "",
        "listings_4_house_id": "",
        "listings_4_listing_board_id": "",
        "listings_4_price": "",
        "listings_4_start_date": "",
        "listings_4_update_at": "",
        "listings_50_end_date": "",
        "listings_50_event": "",
        "listings_50_house_id": "",
        "listings_50_listing_board_id": "",
        "listings_50_price": "",
        "listings_50_start_date": "",
        "listings_50_update_at": "",
        "listings_51_end_date": "",
        "listings_51_event": "",
        "listings_51_house_id": "",
        "listings_51_listing_board_id": "",
        "listings_51_price": "",
        "listings_51_start_date": "",
        "listings_51_update_at": "",
        "listings_52_end_date": "",
        "listings_52_event": "",
        "listings_52_house_id": "",
        "listings_52_listing_board_id": "",
        "listings_52_price": "",
        "listings_52_start_date": "",
        "listings_52_update_at": "",
        "listings_53_end_date": "",
        "listings_53_event": "",
        "listings_53_house_id": "",
        "listings_53_listing_board_id": "",
        "listings_53_price": "",
        "listings_53_start_date": "",
        "listings_53_update_at": "",
        "listings_54_end_date": "",
        "listings_54_event": "",
        "listings_54_house_id": "",
        "listings_54_listing_board_id": "",
        "listings_54_price": "",
        "listings_54_start_date": "",
        "listings_54_update_at": "",
        "listings_55_end_date": "",
        "listings_55_event": "",
        "listings_55_house_id": "",
        "listings_55_listing_board_id": "",
        "listings_55_price": "",
        "listings_55_start_date": "",
        "listings_55_update_at": "",
        "listings_56_end_date": "",
        "listings_56_event": "",
        "listings_56_house_id": "",
        "listings_56_listing_board_id": "",
        "listings_56_price": "",
        "listings_56_start_date": "",
        "listings_56_update_at": "",
        "listings_57_end_date": "",
        "listings_57_event": "",
        "listings_57_house_id": "",
        "listings_57_listing_board_id": "",
        "listings_57_price": "",
        "listings_57_start_date": "",
        "listings_57_update_at": "",
        "listings_58_end_date": "",
        "listings_58_event": "",
        "listings_58_house_id": "",
        "listings_58_listing_board_id": "",
        "listings_58_price": "",
        "listings_58_start_date": "",
        "listings_58_update_at": "",
        "listings_59_end_date": "",
        "listings_59_event": "",
        "listings_59_house_id": "",
        "listings_59_listing_board_id": "",
        "listings_59_price": "",
        "listings_59_start_date": "",
        "listings_59_update_at": "",
        "listings_5_end_date": "",
        "listings_5_event": "",
        "listings_5_house_id": "",
        "listings_5_listing_board_id": "",
        "listings_5_price": "",
        "listings_5_start_date": "",
        "listings_5_update_at": "",
        "listings_60_end_date": "",
        "listings_60_event": "",
        "listings_60_house_id": "",
        "listings_60_listing_board_id": "",
        "listings_60_price": "",
        "listings_60_start_date": "",
        "listings_60_update_at": "",
        "listings_61_end_date": "",
        "listings_61_event": "",
        "listings_61_house_id": "",
        "listings_61_listing_board_id": "",
        "listings_61_price": "",
        "listings_61_start_date": "",
        "listings_61_update_at": "",
        "listings_62_end_date": "",
        "listings_62_event": "",
        "listings_62_house_id": "",
        "listings_62_listing_board_id": "",
        "listings_62_price": "",
        "listings_62_start_date": "",
        "listings_62_update_at": "",
        "listings_63_end_date": "",
        "listings_63_event": "",
        "listings_63_house_id": "",
        "listings_63_listing_board_id": "",
        "listings_63_price": "",
        "listings_63_start_date": "",
        "listings_63_update_at": "",
        "listings_64_end_date": "",
        "listings_64_event": "",
        "listings_64_house_id": "",
        "listings_64_listing_board_id": "",
        "listings_64_price": "",
        "listings_64_start_date": "",
        "listings_64_update_at": "",
        "listings_65_end_date": "",
        "listings_65_event": "",
        "listings_65_house_id": "",
        "listings_65_listing_board_id": "",
        "listings_65_price": "",
        "listings_65_start_date": "",
        "listings_65_update_at": "",
        "listings_66_end_date": "",
        "listings_66_event": "",
        "listings_66_house_id": "",
        "listings_66_listing_board_id": "",
        "listings_66_price": "",
        "listings_66_start_date": "",
        "listings_66_update_at": "",
        "listings_6_end_date": "",
        "listings_6_event": "",
        "listings_6_house_id": "",
        "listings_6_listing_board_id": "",
        "listings_6_price": "",
        "listings_6_start_date": "",
        "listings_6_update_at": "",
        "listings_7_end_date": "",
        "listings_7_event": "",
        "listings_7_house_id": "",
        "listings_7_listing_board_id": "",
        "listings_7_price": "",
        "listings_7_start_date": "",
        "listings_7_update_at": "",
        "listings_8_end_date": "",
        "listings_8_event": "",
        "listings_8_house_id": "",
        "listings_8_listing_board_id": "",
        "listings_8_price": "",
        "listings_8_start_date": "",
        "listings_8_update_at": "",
        "listings_9_end_date": "",
        "listings_9_event": "",
        "listings_9_house_id": "",
        "listings_9_listing_board_id": "",
        "listings_9_price": "",
        "listings_9_start_date": "",
        "listings_9_update_at": "",
        "rooms_0_house_id": "1",
        "rooms_0_level": " Main",
        "rooms_0_type": "Kitchen",
        "rooms_10_house_id": "",
        "rooms_10_level": "",
        "rooms_10_type": "",
        "rooms_11_house_id": "",
        "rooms_11_level": "",
        "rooms_11_type": "",
        "rooms_12_house_id": "",
        "rooms_12_level": "",
        "rooms_12_type": "",
        "rooms_13_house_id": "",
        "rooms_13_level": "",
        "rooms_13_type": "",
        "rooms_14_house_id": "",
        "rooms_14_level": "",
        "rooms_14_type": "",
        "rooms_15_house_id": "",
        "rooms_15_level": "",
        "rooms_15_type": "",
        "rooms_16_house_id": "",
        "rooms_16_level": "",
        "rooms_16_type": "",
        "rooms_17_house_id": "",
        "rooms_17_level": "",
        "rooms_17_type": "",
        "rooms_18_house_id": "",
        "rooms_18_level": "",
        "rooms_18_type": "",
        "rooms_19_house_id": "",
        "rooms_19_level": "",
        "rooms_19_type": "",
        "rooms_1_house_id": "1.0",
        "rooms_1_level": " Main",
        "rooms_1_type": "Living",
        "rooms_20_house_id": "",
        "rooms_20_level": "",
        "rooms_20_type": "",
        "rooms_21_house_id": "",
        "rooms_21_level": "",
        "rooms_21_type": "",
        "rooms_22_house_id": "",
        "rooms_22_level": "",
        "rooms_22_type": "",
        "rooms_23_house_id": "",
        "rooms_23_level": "",
        "rooms_23_type": "",
        "rooms_24_house_id": "",
        "rooms_24_level": "",
        "rooms_24_type": "",
        "rooms_25_house_id": "",
        "rooms_25_level": "",
        "rooms_25_type": "",
        "rooms_26_house_id": "",
        "rooms_26_level": "",
        "rooms_26_type": "",
        "rooms_27_house_id": "",
        "rooms_27_level": "",
        "rooms_27_type": "",
        "rooms_28_house_id": "",
        "rooms_28_level": "",
        "rooms_28_type": "",
        "rooms_29_house_id": "",
        "rooms_29_level": "",
        "rooms_29_type": "",
        "rooms_2_house_id": "1.0",
        "rooms_2_level": " Main",
        "rooms_2_type": "Bathroom",
        "rooms_3_house_id": "1.0",
        "rooms_3_level": " Main",
        "rooms_3_type": "2nd Br",
        "rooms_4_house_id": "1.0",
        "rooms_4_level": " Main",
        "rooms_4_type": "3rd Br",
        "rooms_5_house_id": "",
        "rooms_5_level": "",
        "rooms_5_type": "",
        "rooms_6_house_id": "",
        "rooms_6_level": "",
        "rooms_6_type": "",
        "rooms_7_house_id": "",
        "rooms_7_level": "",
        "rooms_7_type": "",
        "rooms_8_house_id": "",
        "rooms_8_level": "",
        "rooms_8_type": "",
        "rooms_9_house_id": "",
        "rooms_9_level": "",
        "rooms_9_type": "",
        "listed_price": "1998000.0",
        "sold_price": "2405000.0",
        "url": "https://housesigma.com/web/en/house/Vwod7vrNRpo75mGN/162-May-Ave-Richmond-Hill-L4C3S6-N5483762"
    }

    json_variable_getting(hn)


    # result = get_all_data()

    # insert_many()

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