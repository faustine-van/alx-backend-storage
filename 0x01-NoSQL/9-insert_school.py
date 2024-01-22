#!/usr/bin/env python3
"""inserts a new document in a
   collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
   """ function that inserts a new document in a collection
       based on kwargs:
       Returns the new _id
   """
   mongo_collection.insert_many([kwargs])

   return kwargs.get('_id')
