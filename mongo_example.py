# -*- coding: utf-8 -*-
"""
Created on Sun May  1 18:50:01 2016

@author: kia
"""
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://mongodb0.example.net:27019")

db = client['primer']

coll = db.test

#================================

from pymongo import MongoClient

client = MongoClient()
db = client.test

from datetime import datetime
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

result.inserted_id


#========================

from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.restaurants.find()


for document in cursor:
    print(document)
    
cursor = db.restaurants.find({"borough": "Manhattan"})
for document in cursor:
    print(document)
    
    
cursor = db.restaurants.find({"address.zipcode": "10075"})
for document in cursor:
    print(document)
    
    
cursor = db.restaurants.find({"name": "Le Moulin A Cafe"})
for document in cursor:
    print(document)
    

cursor = db.restaurants.find({"grades.grade": "B"})
for document in cursor:
    print(document)

cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
for document in cursor:
    print(document)
    
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})
for document in cursor:
    print(document)
    
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
for document in cursor:
    print(document)


cursor = db.restaurants.find({"$or": [{"cuisine": "Italian"},
                                      {"address.zipcode": "10075"}]})
for document in cursor:
    print(document)
    

import pymongo
cursor = db.restaurants.find().sort([("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)])

for document in cursor:
    print(document)
    

#=============================

from pymongo import MongoClient

client = MongoClient()
db = client.test

result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count

cursor = db.restaurants.find({"name": "Juni"})

for document in cursor:
    print(document)


result = db.restaurants.update_one(
    {"restaurant_id": "41156888"},
    {"$set": {"address.street": "East 31st Street"}}
)

result.matched_count


result = db.restaurants.update_many(
    {"address.zipcode": "10016", "cuisine": "Other"},
    {
        "$set": {"cuisine": "Category To Be Determined"},
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count


result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)

result.matched_count


#==Data Aggregation with PyMongo¶

from pymongo import MongoClient

client = MongoClient()

db = client.test

cursor = db.restaurants.aggregate(
    [
        {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
    ])

for document in cursor:
    print(document)
    

cursor = db.restaurants.aggregate(
    [
        {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
    ]
)

for document in cursor:
    print(document)


#==Indexes with PyMongo

