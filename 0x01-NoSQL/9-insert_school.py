#!/usr/bin/env python3
"""inserts a new document in a
   collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
   """ function that inserts a new document in a collection
       based on kwargs:
       Returns the new _id
   """
   for key, val in enumerate(kwargs):
      mongo_collection.insert_many({key: val})
