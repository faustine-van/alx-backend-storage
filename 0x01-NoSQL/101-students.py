#!/usr/bin/env python3
""" function that returns all 
    students sorted by average score
"""

def top_students(mongo_collection):
     """
      returns all students sorted by average score:
     """
     pipeline = [
       {
         '$unwind': '$topics',
       },
       {
        '$group': {
          '_id':  '$_id',
          'averageScore': {'$avg': '$topics.score'},
          'name': {'$first': '$name'},
         }
       },
       {'$sort': {'averageScore': -1}}
   ]

     return mongo_collection.aggregate(pipeline)
