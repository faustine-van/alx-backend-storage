#!/usr/bin/env python3
"""function that lists all documents
   in a collection
"""


def list_all(mongo_collection):
   """ lists all documents in a collection
       mongo_collection will be the pymongo collection object
   """
   has_doc = bool(mongo_collection.find_one({}))

   if not has_doc:
       return []
   else:
       return mongo_collection.find()
