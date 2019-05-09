#https://github.com/georgetown-analytics/XBUS-502-01.Data_Sources_Storage/blob/master/mongodb_tutorial/MongoDBTutorial.ipynb

import json
import pymongo
from pprint import pprint



'''

Connect

Just as with the relational database example with sqlite, we need to begin by setting up a connection. With MongoDB, we will be using pymongo, though MongoDB also comes with a console API that uses Javascript.

Make sure you have launched Mongo on your system before you connect.

OS X - mongod

Windows - "C:\Program Files\MongoDB\Server\3.2\bin\mongod.exe"

To make our connection, we will use the PyMongo method MongoClient:
'''

conn=pymongo.MongoClient()


#Create and access a database: Mongodb creates databases and collections automatically for you if they don't exist already. A single instance of MongoDB can support multiple independent databases. When working with PyMongo, we access databases using attribute style access, just like we did with sqlite:

db = conn.mydb

conn.database_names()


#A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database. Getting a collection in PyMongo works the same as getting a database:
collection = db.my_collection

db.collection_names()

'''

Insert data

To insert some data into MongoDB, all we need to do is create a dict and call insert_one on the collection object:
'''

doc = {"class":"xbus-502","date":"03-05-2016","instructor":"bengfort","classroom":"C222","roster_count":"25"}
collection.insert_one(doc)

doc = {"class":"xbus-502","date":"03-05-2016","teaching_assistant":"bilbro", "sauce": "awesome"}
collection.insert_one(doc)

'''
A practical example

Rebecca Bilbro, former teaching assistant and current Visual Analytics instructor, has created this practical example for us to work through.

At my job I have been working on a project to help make Commerce datasets easier to find. One of the barriers to searching for records is when the keywords return either too many or too few results. It can also be a problem if the keywords are too technical for lay users.

One solution is to use topic modeling to extract latent themes from the metadata records and then probabilistically assign each record a more sensical set of keywords based on its proximity (via kmeans) to the topics.

In order to get started, first I had to gather up a bunch of JSON metadata records and store them for analysis and modeling. Here's what I did:'

'''

with open("data_sample.json") as data_file:    
    noaa = json.load(data_file)

len(noaa)