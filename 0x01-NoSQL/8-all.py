#!/usr/bin/env python3
"""function that lists all documents
   in a collection
"""


def list_all(mongo_collection):
   """ lists all documents in a collection
       mongo_collection will be the pymongo collection object
   """
   if mongo_collection.count() == 0:
       return []
   return mongo_collection.find()
